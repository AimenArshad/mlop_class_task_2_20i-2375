class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enrollStudents(self, count):
        self.total_strength += count

    def dropStudents(self, count):
        self.total_strength -= count
        if self.total_strength < 0:
            self.total_strength = 0

    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return self.class_name

if __name__ == "__main__":
    ml_ops_class = StudentsInMLOps()
    ml_ops_class.enrollStudents(10)
    print("Total strength after enrollment:", ml_ops_class.getTotalStrength())
    ml_ops_class.dropStudents(3)
    print("Total strength after dropping students:", ml_ops_class.getTotalStrength())
    print("Class name:", ml_ops_class.getClassName())
