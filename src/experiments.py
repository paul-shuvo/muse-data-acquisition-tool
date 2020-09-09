from util import vid_player

experiment_args = {
            'Experiment 1': 
                {
                    'video_path': 'Exp1.mp4'
                },
            'Experiment 2': 
                {
                    'video_path': 'Exp2.mp4'
                },
            'Experiment 3':
                {
                    'video_path': 'Exp3.mp4'
                },
            'Experiment 4':
                {
                    'video_path': 'Exp4.mp4'
                },
            'Experiment 5':
                {
                    'video_path': 'Exp5.mp4'
                },
            'Experiment 6':
                {
                    'video_path': 'Exp6.mp4'
                }
        }

class Experiments:
    def __init__(self, experiment_args=None):
        self.experiment_args = experiment_args
        
    def start_experiment(self, experiment_num, file_name):
        video_path = self.experiment_args[experiment_num]['video_path']
        #fileName=str(fileName)
        vid_player(video_path, file_name)
        
    def add_experiment(self, experiment_args):
        pass