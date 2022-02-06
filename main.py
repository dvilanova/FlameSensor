def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
    music.stop_all_sounds()
    control.reset()
input.on_button_pressed(Button.A, on_button_pressed_a)

FlameVal = 0
led.set_brightness(50)
basic.show_icon(IconNames.SMALL_DIAMOND)
led.set_brightness(150)
basic.show_icon(IconNames.TARGET)
led.set_brightness(255)
basic.show_icon(IconNames.TARGET)
led.stop_animation()
led.set_brightness(50)
basic.show_icon(IconNames.SMALL_DIAMOND)
led.set_brightness(150)
basic.show_icon(IconNames.TARGET)
led.set_brightness(255)
basic.show_icon(IconNames.TARGET)
basic.pause(500)

def on_forever():
    global FlameVal
    FlameVal = pins.digital_read_pin(DigitalPin.P1)
    if FlameVal != 1:
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P2, 1)
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.pause(500)
        while FlameVal != 1:
            led.stop_animation()
            basic.show_string("RUN")
basic.forever(on_forever)
