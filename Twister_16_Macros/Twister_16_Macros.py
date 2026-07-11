# Twister_16_Macros - MIDI Remote Script
# Generated with midiremotescripts.structure-void.com/generator
# This generated script is yours: public domain (CC0 1.0), no restrictions.

from __future__ import absolute_import
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.SliderElement import SliderElement
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from _Framework.EncoderElement import EncoderElement
from _Framework.DeviceComponent import DeviceComponent

class Twister_16_Macros(ControlSurface):

    def __init__(self, c_instance):
        super(Twister_16_Macros, self).__init__(c_instance)
        with self.component_guard():
            self._build()

    def _build(self):
        device = DeviceComponent()
        self.set_device_component(device)  # follows the "blue hand" appointed device

        # CC 0 (ch 2) -> Device — on/off
        el_1 = ButtonElement(True, MIDI_CC_TYPE, 1, 0)
        device.set_on_off_button(el_1)

        # device bank ×16 (absolute) -> selected device parameters
        enc_1_1 = EncoderElement(MIDI_CC_TYPE, 0, 0, Live.MidiMap.MapMode.absolute)
        enc_1_2 = EncoderElement(MIDI_CC_TYPE, 0, 1, Live.MidiMap.MapMode.absolute)
        enc_1_3 = EncoderElement(MIDI_CC_TYPE, 0, 2, Live.MidiMap.MapMode.absolute)
        enc_1_4 = EncoderElement(MIDI_CC_TYPE, 0, 3, Live.MidiMap.MapMode.absolute)
        enc_1_5 = EncoderElement(MIDI_CC_TYPE, 0, 4, Live.MidiMap.MapMode.absolute)
        enc_1_6 = EncoderElement(MIDI_CC_TYPE, 0, 5, Live.MidiMap.MapMode.absolute)
        enc_1_7 = EncoderElement(MIDI_CC_TYPE, 0, 6, Live.MidiMap.MapMode.absolute)
        enc_1_8 = EncoderElement(MIDI_CC_TYPE, 0, 7, Live.MidiMap.MapMode.absolute)
        enc_1_9 = EncoderElement(MIDI_CC_TYPE, 0, 8, Live.MidiMap.MapMode.absolute)
        enc_1_10 = EncoderElement(MIDI_CC_TYPE, 0, 9, Live.MidiMap.MapMode.absolute)
        enc_1_11 = EncoderElement(MIDI_CC_TYPE, 0, 10, Live.MidiMap.MapMode.absolute)
        enc_1_12 = EncoderElement(MIDI_CC_TYPE, 0, 11, Live.MidiMap.MapMode.absolute)
        enc_1_13 = EncoderElement(MIDI_CC_TYPE, 0, 12, Live.MidiMap.MapMode.absolute)
        enc_1_14 = EncoderElement(MIDI_CC_TYPE, 0, 13, Live.MidiMap.MapMode.absolute)
        enc_1_15 = EncoderElement(MIDI_CC_TYPE, 0, 14, Live.MidiMap.MapMode.absolute)
        enc_1_16 = EncoderElement(MIDI_CC_TYPE, 0, 15, Live.MidiMap.MapMode.absolute)
        device.set_parameter_controls([enc_1_1, enc_1_2, enc_1_3, enc_1_4, enc_1_5, enc_1_6, enc_1_7, enc_1_8, enc_1_9, enc_1_10, enc_1_11, enc_1_12, enc_1_13, enc_1_14, enc_1_15, enc_1_16])

    def disconnect(self):
        super(Twister_16_Macros, self).disconnect()
