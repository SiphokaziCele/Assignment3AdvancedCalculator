from Calculations import Calculation

class Graph(Calculation):
    def _init_(self, graphID, functionExpression):
          super()._init_(graphID, functionExpression)
          self.graphImage = None

    def generateGraph(self):
         self.graphImage= f"Graph of {self.expression}"
    def renderGraph(self):
         print (f"Rendering: {self.graphImage}")

    