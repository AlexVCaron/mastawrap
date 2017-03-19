class WorkforceManager:
    pass


class Foreman:
    project = None
    workbook = dict()
    workforceManager = []

    def __init__(self, foreman):
        fields = self.__class__.__dict__.keys()
        for field in foreman:
            self.__setattr__(field, foreman[field]) if field in fields else None

    def assignProject(self, project):
        self.project = project

    def createTask(self, task):
        self.workbook[task.id] = task.task

    def enrollManager(self, count):
        self.workforceManager.extend([WorkforceManager() for i in range(count)])

    # Enrolls workforce for specific managers specified in specs by a certain ratio each
    # on the overall supplied count. Remaining workforce from ratios calculation are
    # distributed evenly starting from the beginning of the list
    def enrollWorkforce(self, count, specs):
        counts = {spec.id: {"count": spec["ratio"] * count, "spec": spec} for spec in specs}
        rem = count - sum([count["count"] for count in counts.values()])
        for i in range(rem - 1):
            counts[i]["count"] += 1
        for count in counts:
            self._enrollWorkforceSpec(count["count"], count["spec"])

    def _enrollWorkforceSpec(self, count, spec):
        manager = self._fetchManager(spec["manager"])

    def _fetchManager(self, managerType):
        pass

