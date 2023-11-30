import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt

from typing import Optional, List, Union
ArrayListType = Union[List, npt.NDArray]

"""
Simple 2D time-discrete robot simulator using linearised motion model
Simon Schwaiger, 2023
"""

landmarks = {
    "a": [1, 1],
    "b": [2, 1],
    "c": [3, 1],
    "d": [1, 2],
    "e": [1, 2],
    "f": [1, 3],
    "g": [2, 2],
    "h": [3, 3]
}

def plotEnv(landmarks=None, states=None, measurement=None, estimatedStates=None) -> None:
    fig, ax = plt.subplots()
    if landmarks is not None:
        for code, (x, y) in landmarks.items():
            ax.annotate(code, (x-0.007, y-0.007))
            ax.scatter(x, y, s=180, facecolors='none', edgecolors='r')
    if states is not None:
        for s in states:
            p2 = np.array([
                s[0] + np.cos(s[2]),
                s[1] + np.sin(s[2])
            ])
            p2 /= np.linalg.norm(p2)*4
            ax.arrow(s[0], s[1], p2[0], p2[1], width=0.02, label="Actual Robot State")
    if estimatedStates is not None:
        ax.plot(np.array(estimatedStates)[:,0], np.array(estimatedStates)[:,1], c="steelblue", label="Estimated Robot Path")
    if measurement is not None and states is not None: # Requires latest state for plotting
        s = states[-1]
        for m in measurement:
            x2 = s[0] + np.cos(s[2] + m[1])*m[0] # landmark x = robotx + cos(theta + bearing)*range
            y2 = s[1] + np.sin(s[2] + m[1])*m[0] # landmark y = roboty + sin(theta + bearing)*range
            ax.plot([s[0], x2], [s[1], y2], c="lightgrey", label="Latest Measurement") 
    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    #ax.legend()
    plt.show()

class robotSim:
    def __init__(self, initialPose, dt) -> None:
        self.pose: ArrayListType = initialPose
        self.dt: float = dt
    def move(self, cmdVel):
        self.pose = self.movementUpdate(self.pose, cmdVel=cmdVel, dt=self.dt)
        return self.pose, self.sensorUpdate(self.pose)
    @staticmethod
    def movementUpdate(pose: ArrayListType, cmdVel: Optional[ArrayListType]=None, dt: float=0.1) -> ArrayListType:
        newPose = np.array(pose, dtype=np.float32)
        if cmdVel != None:
            ## Apply simplified linear motion model with significant error
            newPose += np.array([
                np.cos(newPose[2]) * cmdVel[0] * dt,
                np.sin(newPose[2]) * cmdVel[0] * dt,
                cmdVel[1] * dt
            ], dtype=np.float32)# + (np.random.rand(3)-0.5)/10 # Error term
        return newPose
    @staticmethod
    def sensorUpdate(pose: ArrayListType) -> ArrayListType:
        # measurement = [range, bearing, signature]
        ret = []
        for code, (l_x, l_y) in landmarks.items():
            l_r = np.sqrt((l_x - pose[0])**2 + (l_y - pose[1])**2)# + float((np.random.rand(1)-0.5)/10) # range with error term
            l_b = np.arctan2( l_y - pose[1], l_x - pose[0]) # bearing
            l_b = l_b - pose[2]
            if l_b < -np.pi: l_b += 2*np.pi
            elif l_b > np.pi: l_b -= 2*np.pi
            ret.append([l_r, l_b, code]) # [range, bearing, signature], Thrun S.178
        return sorted(ret, key=lambda x: (x[0]))


dt = 1.0 # Delta time [sec]
initialState = [0, 0, 0] # [x, y, theta]

commands = [ # [x', theta']
    [0.4, 0],
    [0.1, 0.8],
    [0.5, 0.5],
    [0.2, 0.3],
    [0.2, 0.4],
    [0.4, -1.2],
    [0.2, -0.6],
    [0.1, 0.4],
    [0.4, 0.5],
    [0.2, 0.2],
    [0.1, 0.1],
    [0.3, 0],
    [0.4, 0],
    [0.2, -1.4],
    [0.2, -0.2],
    [0.5, -1.0],
    [0.5, 0],
    [0.5, 0]
]

sim = robotSim(initialState, dt)
simRet = np.array([ sim.move(command) for command in commands ], dtype="object")
realStates = np.array(simRet[:,0].tolist(), dtype=np.float32).tolist()
measurements = simRet[:,1].tolist()