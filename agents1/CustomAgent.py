import random
from agents1.OfficialAgent import BaselineAgent

class CustomBaselineAgent(BaselineAgent):
    def __init__(self, slowdown, condition, name, folder, trust_mode='random'):
        self.trust_mode = trust_mode
        super().__init__(slowdown, condition, name, folder)

    def _loadBelief(self):
        if self.trust_mode == 'always_lies':
            value = -1
        elif self.trust_mode == 'always_truth':
            value = 1
        elif self.trust_mode == 'random':
            value = random.choice([-1, 1])
        else:
            value = random.choice([-1, 1])

        self._trusts[self._human_name] = {
            'search': {'competence': value, 'willingness': value},
            'rescue': {'competence': value, 'willingness': value}
        }
    
    def _trustBelief(self, task, competence_change=0, willingness_change=0):
        '''
        Baseline implementation of a trust belief. Creates a dictionary with trust belief scores for each team member, for example based on the received messages.
        '''
        self._trusts[self._human_name][task]['competence'] = np.clip(self._trusts[self._human_name][task]['competence'], -1, 1)
        self._trusts[self._human_name][task]['willingness'] = np.clip(self._trusts[self._human_name][task]['willingness'], -1, 1)
        
        # Save current trust belief values so we can later use and retrieve them to add to a csv file with all the logged trust belief values
        with open(self._folder + '/beliefs/currentTrustBelief.csv', mode='w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['name', 'competence', 'willingness', 'task'])
            csv_writer.writerow([self._human_name, self._trusts[self._human_name]['search']['competence'],
                                 self._trusts[self._human_name]['search']['willingness'], 'search'])
            csv_writer.writerow([self._human_name, self._trusts[self._human_name]['rescue']['competence'],
                                 self._trusts[self._human_name]['rescue']['willingness'], 'rescue'])
