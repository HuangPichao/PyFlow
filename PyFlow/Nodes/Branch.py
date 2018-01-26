from Qt import QtCore
from AbstractGraph import *
from Settings import *
from Node import Node


class branch(Node, NodeBase):
    def __init__(self, name, graph):
        super(branch, self).__init__(name, graph)
        self.trueExec = self.addOutputPin("True", DataTypes.Exec)
        self.falseExec = self.addOutputPin("False", DataTypes.Exec)
        self.inExec = self.addInputPin("In", DataTypes.Exec, self.compute)
        self.condition = self.addInputPin("condition", DataTypes.Bool)

    @staticmethod
    def pinTypeHints():
        return {'inputs': [DataTypes.Exec, DataTypes.Bool], 'outputs': [DataTypes.Bool]}

    @staticmethod
    def category():
        return 'FlowControl'

    def compute(self):
        data = self.condition.getData()
        if data:
            self.trueExec.call()
        else:
            self.falseExec.call()
