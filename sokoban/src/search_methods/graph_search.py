# class Explorer:
class GraphSearch:
    def set_initial_state(self, state):
        raise NotImplementedError
    
    def next_iter(self):
        raise NotImplementedError
    
    def get_results(self):
        raise NotImplementedError
    
    def has_finished(self):
        raise NotImplementedError
