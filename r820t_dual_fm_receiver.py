#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: R820T Dual Fm Receiver
# Generated: Thu Jul 16 08:25:52 2015
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class r820t_dual_fm_receiver(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="R820T Dual Fm Receiver")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.tune_offset_2 = tune_offset_2 = 0
        self.tune_offset_1 = tune_offset_1 = 0
        self.center_freq = center_freq = 97.9e6
        self.tuned_in_to_0 = tuned_in_to_0 = center_freq+tune_offset_2
        self.tuned_in_to = tuned_in_to = center_freq+tune_offset_1
        self.samp_rate = samp_rate = 2e6
        self.channel_width = channel_width = 200e3
        self.audio_gain = audio_gain = 1

        ##################################################
        # Blocks
        ##################################################
        _tune_offset_2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tune_offset_2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tune_offset_2_sizer,
        	value=self.tune_offset_2,
        	callback=self.set_tune_offset_2,
        	label='tune_offset_2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tune_offset_2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tune_offset_2_sizer,
        	value=self.tune_offset_2,
        	callback=self.set_tune_offset_2,
        	minimum=0-(samp_rate)/2,
        	maximum=(samp_rate)/2,
        	num_steps=int(samp_rate / 200e3),
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_tune_offset_2_sizer, 4, 0, 1, 100)
        _tune_offset_1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tune_offset_1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tune_offset_1_sizer,
        	value=self.tune_offset_1,
        	callback=self.set_tune_offset_1,
        	label='tune_offset_1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tune_offset_1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tune_offset_1_sizer,
        	value=self.tune_offset_1,
        	callback=self.set_tune_offset_1,
        	minimum=0-(samp_rate)/2,
        	maximum=(samp_rate)/2,
        	num_steps=int(samp_rate / 200e3),
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_tune_offset_1_sizer, 2, 0, 1, 100)
        _center_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._center_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_center_freq_sizer,
        	value=self.center_freq,
        	callback=self.set_center_freq,
        	label='center_freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._center_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_center_freq_sizer,
        	value=self.center_freq,
        	callback=self.set_center_freq,
        	minimum=87.9e6,
        	maximum=107.9e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_center_freq_sizer, 1, 0, 1, 100)
        _audio_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._audio_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_audio_gain_sizer,
        	value=self.audio_gain,
        	callback=self.set_audio_gain,
        	label='audio_gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._audio_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_audio_gain_sizer,
        	value=self.audio_gain,
        	callback=self.set_audio_gain,
        	minimum=0,
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_audio_gain_sizer, 0, 0, 1, 100)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=center_freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self._tuned_in_to_0_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.tuned_in_to_0,
        	callback=self.set_tuned_in_to_0,
        	label="Channel 2",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._tuned_in_to_0_static_text, 5, 0, 1, 100)
        self._tuned_in_to_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.tuned_in_to,
        	callback=self.set_tuned_in_to,
        	label="Channel 1",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._tuned_in_to_static_text, 3, 0, 1, 100)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(2, 0)
        self.osmosdr_source_0.set_iq_balance_mode(2, 0)
        self.osmosdr_source_0.set_gain_mode(1, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(int(samp_rate / channel_width), firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(int(samp_rate / channel_width), firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((audio_gain, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((audio_gain, ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_sink_0_0 = audio.sink(48000, "", True)
        self.analog_wfm_rcv_0_0 = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -tune_offset_2, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -tune_offset_1, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_wfm_rcv_0_0, 0))
        self.connect((self.analog_wfm_rcv_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0_0, 0))


# QT sink close method reimplementation

    def get_tune_offset_2(self):
        return self.tune_offset_2

    def set_tune_offset_2(self, tune_offset_2):
        self.tune_offset_2 = tune_offset_2
        self.analog_sig_source_x_0_0.set_frequency(-self.tune_offset_2)
        self._tune_offset_2_slider.set_value(self.tune_offset_2)
        self._tune_offset_2_text_box.set_value(self.tune_offset_2)
        self.set_tuned_in_to_0(self.center_freq+self.tune_offset_2)

    def get_tune_offset_1(self):
        return self.tune_offset_1

    def set_tune_offset_1(self, tune_offset_1):
        self.tune_offset_1 = tune_offset_1
        self.analog_sig_source_x_0.set_frequency(-self.tune_offset_1)
        self._tune_offset_1_slider.set_value(self.tune_offset_1)
        self._tune_offset_1_text_box.set_value(self.tune_offset_1)
        self.set_tuned_in_to(self.center_freq+self.tune_offset_1)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self._center_freq_slider.set_value(self.center_freq)
        self._center_freq_text_box.set_value(self.center_freq)
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)
        self.set_tuned_in_to(self.center_freq+self.tune_offset_1)
        self.set_tuned_in_to_0(self.center_freq+self.tune_offset_2)
        self.wxgui_fftsink2_0.set_baseband_freq(self.center_freq)

    def get_tuned_in_to_0(self):
        return self.tuned_in_to_0

    def set_tuned_in_to_0(self, tuned_in_to_0):
        self.tuned_in_to_0 = tuned_in_to_0
        self._tuned_in_to_0_static_text.set_value(self.tuned_in_to_0)

    def get_tuned_in_to(self):
        return self.tuned_in_to

    def set_tuned_in_to(self, tuned_in_to):
        self.tuned_in_to = tuned_in_to
        self._tuned_in_to_static_text.set_value(self.tuned_in_to)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))

    def get_channel_width(self):
        return self.channel_width

    def set_channel_width(self, channel_width):
        self.channel_width = channel_width

    def get_audio_gain(self):
        return self.audio_gain

    def set_audio_gain(self, audio_gain):
        self.audio_gain = audio_gain
        self._audio_gain_slider.set_value(self.audio_gain)
        self._audio_gain_text_box.set_value(self.audio_gain)
        self.blocks_multiply_const_vxx_0.set_k((self.audio_gain, ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.audio_gain, ))

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = r820t_dual_fm_receiver()
    tb.Start(True)
    tb.Wait()

