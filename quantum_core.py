class QuantumExecutionState:
    def __init__(self):
        self.states = {
            'A': 'Atmosphere',
            'S': 'Surface',
            'R': 'Radiation',
            'M': 'Magnetic'
        }

    def scan(self, state):
        if state in self.states:
            return f'Measurement output for {self.states[state]}: {self.measure(state)}'
        else:
            return 'Invalid state'

    def measure(self, state):
        # Simulating a deterministic measurement output based on the state
        return f'Data from {self.states[state]} scan'

if __name__ == '__main__':
    quantum_scan = QuantumExecutionState()
    for state in quantum_scan.states.keys():
        print(quantum_scan.scan(state))