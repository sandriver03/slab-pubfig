import scipy.io as sio

from pubfig.figclass import FigClass


class Apo_plot(FigClass):

    def __init__(self,
                 fignum=1,
                 style='default',
                 size='A4',
                 size_unit='cm',
                 canvas_format='A4',
                 ):

        FigClass.__init__(self, project='Apo_Data',
                          fignum=fignum,
                          style=style,
                          size=size,
                          size_unit=size_unit,
                          canvas_format=canvas_format)

    def _load_data(self, file_name):
        # need to clean up .mat file...
        print('data is not provided; the purpose of the example is to show the functionality of axes dividing')
        '''
        data = sio.loadmat(file_name)
        simData = data['Data'][0][0]['SimData'][0][0]
        Data_Names = ['SimData', 'SimData_is', 'SimData_rY', 'SimData_rY_is',
                      'SimMap', 'SimMap_is', 'SimMap_rY', 'SimMap_rY_is']
        _c_data = dict()
        for n in Data_Names:
            _c_data[n] = simData[n][0][0]

        self.data = _c_data
        '''

    def _prepare_axes(self):
        self._init_fig()
        self.divide_axes(Y0=(0.5, 0.45), DivX=(1, 2, 1, 2), SepXs=(0.5, 1, 0.5), DivY=2, SepYs=0.5)
        self.axes[0][0][0].set_xlim([-160, 160])
        self.axes[0][0][0].set_xticks([-150, 0, 150])
        self.axes[0][0][0].set_ylim([-610, 10])
        self.axes[0][0][0].set_yticks([-600, -300, 0])
        self.axes[0][0][0].set_ylabel(r'Cortical depth ($\mu$m)')
        self.add_label('A', ref=self.axes[0][0][0])

        _, axes = self.divide_axes(target=self.axes[0][0][1], DivX=(5, 1), SepXs=0.2, DivY=(1, 5), SepYs=0.2)
        axes[0][1].remove()
        axes[0][0].set_xlim([-100, 100])
        axes[0][0].set_xticks([-80, 0, 80])
        axes[0][0].set_xticklabels([])
        axes[0][0].set_ylim([0.9, 1.1])
        axes[0][0].set_yticks([0.9, 1.0, 1.1])
        axes[0][0].set_yticklabels([0.9, None, 1.1])

        axes[1][0].set_xlim([-100, 100])
        axes[1][0].set_xticks([-80, 0, 80])
        axes[1][0].set_ylim([-100, 100])
        axes[1][0].set_yticks([-80, 0, 80])
        axes[1][0].set_xlabel(r'Cortical width ($\mu$m)')

        axes[1][1].set_xlim([0.9, 1.1])
        axes[1][1].set_xticks([0.9, 1.0, 1.1])
        axes[1][1].set_xticklabels([0.9, None, 1.1])
        axes[1][1].set_ylim([-100, 100])
        axes[1][1].set_yticks([-80, 0, 80])
        axes[1][1].set_yticklabels([])



