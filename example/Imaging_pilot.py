import numpy as np
import os
import matplotlib.pyplot as plt
import scipy.ndimage as s_image

from pubfig.figclass import FigClass


class Imaging_pilot(FigClass):

    def __init__(self,
                 fignum=1,
                 style='default',
                 size='A4',
                 size_unit='cm',
                 canvas_format='A4',
                 ):

        FigClass.__init__(self, project='Imaging_Pilot',
                          fignum=fignum,
                          style=style,
                          size=size,
                          size_unit=size_unit,
                          canvas_format=canvas_format)

    def load_data(self, fnames=None):

        print('data is not provided; the purpose of the example is to show the functionality of axes dividing\n')
        print('the resulting figure can be seen in Figure_1.png')

        '''
        # data are saved with np.savez
        if fnames is None:
            fnames = ['pilot_calcium_whitenoise.npz', 'pilot_ISI_whitenoise.npz',
                      'pilot_calcium_tone.npz', 'pilot_ISI_tone.npz']

        data_dir = self._data_dir
        self.data = []
        count = 0
        for fn in fnames:
            with np.load(os.path.join(data_dir, fn), allow_pickle=True) as fh:
                data = {}
                for d in fh.items():
                    data[d[0]] = d[1]
                self.data.append(data)
                count += 1
        '''

    def _prepare_axes(self):
        self._init_fig()
        # divide the canvas into 2 rows,  with 1:1:2 division
        # self.divide_axes(Y0=(0.62, 0.32), DivY=2, SepYs=0.5, DivX=(1, 1, 2), SepXs=0.5)

        # divide the canvas into 3 rows, first row with 2 columns, 2nd row with 4 and 3rd with 2
        self.divide_axes(Y0=(0.42, 0.52), DivY=3, SepYs=0.2, DivX=1)

        # divide first row into 3 columns
        _, axes0 = self.divide_axes(target=self.axes[0][0][0], X0=(0.1, 0.8), DivX=3, SepXs=0.5, DivY=1)
        self.add_label('A', ref=axes0[0][0])
        self.add_label('B', ref=axes0[0][1])
        self.add_label('C', ref=axes0[0][2])
        # leave A blank, space reserved for schematic drawing
        # axes0[0][0].axes.set_axis_off()
        # B is the green channel image, used as background; no axis is needed
        # axes0[0][1].axes.set_axis_off()
        # bg_img = self.data[0]['bg']
        # axes0[0][1].imshow(bg_img, cmap='gray', clim=[0, 25000])
        axes0[0][1].set_title('Green illumination')
        # C is the white noise result; no axis is needed
        # wn_img = self.data[0]['res_img']
        # im = axes0[0][2].imshow(wn_img, cmap='viridis', clim=[-0.5e-2, 2e-2])
        # axes0[0][2].axes.set_axis_off()
        axes0[0][2].set_title('White noise')
        # colorbar
        cb_ax = axes0[0][2].figure.add_axes([0.875, 0.796, 0.02, 0.133])
        # plt.colorbar(im, cax=cb_ax)
        # add text to colorbar scale
        self.add_text(r"$\Delta$F/F", pos=[0.905, 0.94], fontdict={'size':10})

        # divide 2nd row into 4 columns
        _, axes1 = self.divide_axes(target=self.axes[0][1][0], DivX=4, SepXs=0.3, DivY=1)
        # add subfig labels
        self.add_label('D1', ref=axes1[0][0])
        self.add_label('D2', ref=axes1[0][3])
        # 4 plots for 4k, 8k, 16k and tonotopy
        # res_4k = self.data[2]['res_img'].item()[4]
        # res_8k = self.data[2]['res_img'].item()[8]
        # res_16k = self.data[2]['res_img'].item()[16]
        # img_ton = np.zeros((512, 512, 3))
        # img_ton[:, :, 0] = res_4k / np.max(res_4k)
        # img_ton[:, :, 1] = res_8k / np.max(res_8k)
        # img_ton[:, :, 2] = res_16k / np.max(res_16k)
        # img_ton[img_ton < 0.3] = 0
        # or, calculate prefered tone for each pixel
        # img_ton_prefer = np.zeros([512, 512, 3])
        # img_ton_prefer[img_ton[:, :, 0] == np.max(img_ton, 2), 0] = 1
        # img_ton_prefer[img_ton[:, :, 1] == np.max(img_ton, 2), 1] = 1
        # img_ton_prefer[img_ton[:, :, 2] == np.max(img_ton, 2), 2] = 1
        # img_ton_prefer[img_ton.mean(2) < 0.15] = 1
        # img_ton_p2 = (img_ton_prefer.copy() * np.array([4, 8, 16])).sum(2)
        # img_ton_p2[img_ton.mean(2) < 0.15] = np.nan
        # axes1[0][0].imshow(res_4k, cmap='viridis', clim=[-0.5e-2, 2e-2])
        # axes1[0][0].axes.set_axis_off()
        axes1[0][0].set_title('4 kHz')
        # axes1[0][1].imshow(res_8k, cmap='viridis', clim=[-0.5e-2, 2e-2])
        # axes1[0][1].axes.set_axis_off()
        axes1[0][1].set_title('8 kHz')
        # axes1[0][2].imshow(res_16k, cmap='viridis', clim=[-0.5e-2, 2e-2])
        # axes1[0][2].axes.set_axis_off()
        axes1[0][2].set_title('16 kHz')
        # TODO: overlay tonotopy with background image?
        # axes1[0][3].imshow(img_ton)
        # axes1[0][3].axes.set_axis_off()
        # TODO: colorbar

        # divide 3rd row into 2 columns
        _, axes2 = self.divide_axes(target=self.axes[0][2][0], DivX=2, SepXs=0.5, DivY=1)
        self.add_label('E1', ref=axes2[0][0])
        self.add_label('E2', ref=axes2[0][1])
        # E1, time course of 2 points, from white noise stimulation
        tm = np.linspace(-0.95, 4.05, 51)
        # data_in = self.data[0]['res_t0']
        # data_out = self.data[0]['res_t1']
        # avg = np.mean(data_out, (2, 0))
        avg = np.random.randn(*tm.shape)
        # ste = np.std(data_out, (2, 0)) / np.sqrt(data_out.shape[0])
        ste = 0.1*np.random.randn(*tm.shape)
        axes2[0][0].plot(tm, avg, color=[0.7, 0.7, 0.7])
        axes2[0][0].fill_between(tm, avg + ste, avg - ste, color=[0.7, 0.7, 0.7], alpha=0.3)
        # avg = np.mean(data_in, (2, 0))
        # ste = np.std(data_in, (2, 0)) / np.sqrt(data_out.shape[0])
        avg = np.random.randn(*tm.shape)
        ste = 0.1*np.random.randn(*tm.shape)
        axes2[0][0].plot(tm, avg, color=[0.1, 0.1, 0.1])
        axes2[0][0].fill_between(tm, avg + ste, avg - ste, color=[0.1, 0.1, 0.1], alpha=0.4)
        axes2[0][0].set_xlim([-1, 3])
        axes2[0][0].set_ylim([-0.01, 0.03])
        axes2[0][0].set_xlabel("time (s)")
        axes2[0][0].set_ylabel(r"$\Delta$F/F")
        axes2[0][0].legend(['P1', 'P2'], edgecolor=[1, 1, 1])
        # stimulation representation
        axes2[0][0].fill_between([0, 1], -0.006, -0.004, color=[0.5, 0.5, 0.5])
        # E2, time course of 3 points, from 4k stimulation
        # data_4 = self.data[2]['res_t4'].item()[4]
        # data_8 = self.data[2]['res_t4'].item()[8]
        # data_16 = self.data[2]['res_t4'].item()[16]
        # avg = np.mean(data_4, (2, 0))
        # ste = np.std(data_4, (2, 0)) / np.sqrt(data_4.shape[0])
        avg = np.random.randn(*tm.shape)
        ste = 0.1*np.random.randn(*tm.shape)
        axes2[0][1].plot(tm, avg, color=[1, 0, 0])
        axes2[0][1].fill_between(tm, avg + ste, avg - ste, color=[1, 0, 0], alpha=0.4)
        # avg = np.mean(data_8, (2, 0)) * 0.8
        # ste = np.std(data_8, (2, 0)) / np.sqrt(data_8.shape[0])
        avg = np.random.randn(*tm.shape)
        ste = 0.1*np.random.randn(*tm.shape)
        axes2[0][1].plot(tm, avg, color=[0, 1, 0])
        axes2[0][1].fill_between(tm, avg + ste, avg - ste, color=[0, 1, 0], alpha=0.4)
        # avg = np.mean(data_16, (2, 0)) * 0.8
        # ste = np.std(data_16, (2, 0)) / np.sqrt(data_16.shape[0])
        avg = np.random.randn(*tm.shape)
        ste = 0.1*np.random.randn(*tm.shape)
        axes2[0][1].plot(tm, avg, color=[0, 0, 1])
        axes2[0][1].fill_between(tm, avg + ste, avg - ste, color=[0, 0, 1], alpha=0.4)
        axes2[0][1].set_xlim([-1, 3])
        axes2[0][1].set_ylim([-0.01, 0.03])
        axes2[0][1].set_xlabel("time (s)")
        axes2[0][1].set_ylabel(r"$\Delta$F/F")
        # stimulation representation
        axes2[0][1].fill_between([0, 1], -0.006, -0.004, color=[0.5, 0.5, 0.5])
        axes2[0][1].legend(['P3', 'P4', 'P5'], edgecolor=[1, 1, 1])
        # box half off
        axes2[0][0].spines['top'].set_visible(False)
        axes2[0][0].spines['right'].set_visible(False)
        axes2[0][1].spines['top'].set_visible(False)
        axes2[0][1].spines['right'].set_visible(False)

    def draw_ISI(self):
        self._init_fig()
        # divide the canvas into 2 rows,  with 1:1:2 division
        # self.divide_axes(Y0=(0.62, 0.32), DivY=2, SepYs=0.5, DivX=(1, 1, 2), SepXs=0.5)

        # divide the canvas into 3 rows, first row with 2 columns, 2nd row with 4 and 3rd with 2
        self.divide_axes(Y0=(0.42, 0.52), DivY=3, SepYs=0.2, DivX=1)

        # divide first row into 3 columns
        _, axes0 = self.divide_axes(target=self.axes[0][0][0], X0=(0.1, 0.8), DivX=3, SepXs=0.5, DivY=1)
        self.add_label('A', ref=axes0[0][0])
        self.add_label('B', ref=axes0[0][1])
        self.add_label('C', ref=axes0[0][2])
        # leave A blank, space reserved for schematic drawing
        # axes0[0][0].axes.set_axis_off()
        # B is the green channel image, used as background; no axis is needed
        # axes0[0][1].axes.set_axis_off()
        # bg_img = self.data[0]['bg']
        # axes0[0][1].imshow(bg_img, cmap='gray', clim=[0, 25000])
        axes0[0][1].set_title('Green illumination')
        # C is the white noise result; no axis is needed
        # wn_img = self.data[0]['res_img']
        # im = axes0[0][2].imshow(wn_img, cmap='viridis', clim=[-0.5e-2, 2e-2])
        # axes0[0][2].axes.set_axis_off()
        axes0[0][2].set_title('White noise')
        # colorbar
        cb_ax = axes0[0][2].figure.add_axes([0.875, 0.796, 0.02, 0.133])
        # plt.colorbar(im, cax=cb_ax)
        # add text to colorbar scale
        self.add_text(r"$\Delta$F/F", pos=[0.905, 0.94], fontdict={'size':10})

        # divide 2nd row into 4 columns
        _, axes1 = self.divide_axes(target=self.axes[0][1][0], DivX=4, SepXs=0.3, DivY=1)
        # add subfig labels
        self.add_label('D1', ref=axes1[0][0])
        self.add_label('D2', ref=axes1[0][3])
        # 4 plots for 4k, 8k, 16k and tonotopy
        # res_4k = self.data[2]['res_img'].item()[4]
        # res_8k = self.data[2]['res_img'].item()[8]
        # res_16k = self.data[2]['res_img'].item()[16]
        # img_ton = np.zeros((512, 512, 3))
        # img_ton[:, :, 0] = res_4k / np.max(res_4k)
        # img_ton[:, :, 1] = res_8k / np.max(res_8k)
        # img_ton[:, :, 2] = res_16k / np.max(res_16k)
        # img_ton[img_ton < 0.3] = 0
        # or, calculate prefered tone for each pixel
        # img_ton_prefer = np.zeros([512, 512, 3])
        # img_ton_prefer[img_ton[:, :, 0] == np.max(img_ton, 2), 0] = 1
        # img_ton_prefer[img_ton[:, :, 1] == np.max(img_ton, 2), 1] = 1
        # img_ton_prefer[img_ton[:, :, 2] == np.max(img_ton, 2), 2] = 1
        # img_ton_prefer[img_ton.mean(2) < 0.15] = 1
        # img_ton_p2 = (img_ton_prefer.copy() * np.array([4, 8, 16])).sum(2)
        # img_ton_p2[img_ton.mean(2) < 0.15] = np.nan
        # axes1[0][0].imshow(res_4k, cmap='viridis', clim=[-0.5e-2, 2e-2])
        # axes1[0][0].axes.set_axis_off()
        axes1[0][0].set_title('4 kHz')
        # axes1[0][1].imshow(res_8k, cmap='viridis', clim=[-0.5e-2, 2e-2])
        # axes1[0][1].axes.set_axis_off()
        axes1[0][1].set_title('8 kHz')
        # axes1[0][2].imshow(res_16k, cmap='viridis', clim=[-0.5e-2, 2e-2])
        # axes1[0][2].axes.set_axis_off()
        axes1[0][2].set_title('16 kHz')
        # TODO: overlay tonotopy with background image?
        # axes1[0][3].imshow(img_ton)
        # axes1[0][3].axes.set_axis_off()
        # TODO: colorbar

        # divide 3rd row into 2 columns
        _, axes2 = self.divide_axes(target=self.axes[0][2][0], DivX=2, SepXs=0.5, DivY=1)
        self.add_label('E1', ref=axes2[0][0])
        self.add_label('E2', ref=axes2[0][1])
        # E1, time course of 2 points, from white noise stimulation
        tm = np.linspace(-0.95, 4.05, 51)
        # data_in = self.data[0]['res_t0']
        # data_out = self.data[0]['res_t1']
        # avg = np.mean(data_out, (2, 0))
        avg = np.random.randn(*tm.shape)
        # ste = np.std(data_out, (2, 0)) / np.sqrt(data_out.shape[0])
        ste = 0.1*np.random.randn(*tm.shape)
        axes2[0][0].plot(tm, avg, color=[0.7, 0.7, 0.7])
        axes2[0][0].fill_between(tm, avg + ste, avg - ste, color=[0.7, 0.7, 0.7], alpha=0.3)
        # avg = np.mean(data_in, (2, 0))
        # ste = np.std(data_in, (2, 0)) / np.sqrt(data_out.shape[0])
        avg = np.random.randn(*tm.shape)
        ste = 0.1*np.random.randn(*tm.shape)
        axes2[0][0].plot(tm, avg, color=[0.1, 0.1, 0.1])
        axes2[0][0].fill_between(tm, avg + ste, avg - ste, color=[0.1, 0.1, 0.1], alpha=0.4)
        axes2[0][0].set_xlim([-1, 3])
        axes2[0][0].set_ylim([-0.01, 0.03])
        axes2[0][0].set_xlabel("time (s)")
        axes2[0][0].set_ylabel(r"$\Delta$F/F")
        axes2[0][0].legend(['P1', 'P2'], edgecolor=[1, 1, 1])
        # stimulation representation
        axes2[0][0].fill_between([0, 1], -0.006, -0.004, color=[0.5, 0.5, 0.5])
        # E2, time course of 3 points, from 4k stimulation
        # data_4 = self.data[2]['res_t4'].item()[4]
        # data_8 = self.data[2]['res_t4'].item()[8]
        # data_16 = self.data[2]['res_t4'].item()[16]
        # avg = np.mean(data_4, (2, 0))
        # ste = np.std(data_4, (2, 0)) / np.sqrt(data_4.shape[0])
        avg = np.random.randn(*tm.shape)
        ste = 0.1*np.random.randn(*tm.shape)
        axes2[0][1].plot(tm, avg, color=[1, 0, 0])
        axes2[0][1].fill_between(tm, avg + ste, avg - ste, color=[1, 0, 0], alpha=0.4)
        # avg = np.mean(data_8, (2, 0)) * 0.8
        # ste = np.std(data_8, (2, 0)) / np.sqrt(data_8.shape[0])
        avg = np.random.randn(*tm.shape)
        ste = 0.1*np.random.randn(*tm.shape)
        axes2[0][1].plot(tm, avg, color=[0, 1, 0])
        axes2[0][1].fill_between(tm, avg + ste, avg - ste, color=[0, 1, 0], alpha=0.4)
        # avg = np.mean(data_16, (2, 0)) * 0.8
        # ste = np.std(data_16, (2, 0)) / np.sqrt(data_16.shape[0])
        avg = np.random.randn(*tm.shape)
        ste = 0.1*np.random.randn(*tm.shape)
        axes2[0][1].plot(tm, avg, color=[0, 0, 1])
        axes2[0][1].fill_between(tm, avg + ste, avg - ste, color=[0, 0, 1], alpha=0.4)
        axes2[0][1].set_xlim([-1, 3])
        axes2[0][1].set_ylim([-0.01, 0.03])
        axes2[0][1].set_xlabel("time (s)")
        axes2[0][1].set_ylabel(r"$\Delta$F/F")
        # stimulation representation
        axes2[0][1].fill_between([0, 1], -0.006, -0.004, color=[0.5, 0.5, 0.5])
        axes2[0][1].legend(['P3', 'P4', 'P5'], edgecolor=[1, 1, 1])
        # box half off
        axes2[0][0].spines['top'].set_visible(False)
        axes2[0][0].spines['right'].set_visible(False)
        axes2[0][1].spines['top'].set_visible(False)
        axes2[0][1].spines['right'].set_visible(False)


# code to get the data file
# np.savez(os.path.join(res_folder, res_file), bg=bg_frame, roi_4=roi_4k, roi_8=roi_8k, roi_16=roi_16k, roi_n=wn_roi1,
# res_t4={4:tc_roi4_t4, 8:tc_roi8_t4, 16:tc_roi16_t4, 0:tc_nores_t4},
# res_t8={4:tc_roi4_t8, 8:tc_roi8_t8, 16:tc_roi16_t8, 0:tc_nores_t8},
# res_t16={4:tc_roi4_t16, 8:tc_roi8_t16, 16:tc_roi16_t16, 0:tc_nores_t16}, res_img={4:res_4k, 8:res_8k, 16:res_16k})
