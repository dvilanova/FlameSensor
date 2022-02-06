input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P2, 0)
    music.stopAllSounds()
    control.reset()
})
let FlameVal = 0
led.setBrightness(50)
basic.showIcon(IconNames.SmallDiamond)
led.setBrightness(150)
basic.showIcon(IconNames.Target)
led.setBrightness(255)
basic.showIcon(IconNames.Target)
led.stopAnimation()
led.setBrightness(50)
basic.showIcon(IconNames.SmallDiamond)
led.setBrightness(150)
basic.showIcon(IconNames.Target)
led.setBrightness(255)
basic.showIcon(IconNames.Target)
basic.pause(500)
basic.forever(function () {
    FlameVal = pins.digitalReadPin(DigitalPin.P1)
    if (FlameVal != 1) {
        basic.pause(500)
        pins.digitalWritePin(DigitalPin.P2, 1)
        pins.digitalWritePin(DigitalPin.P0, 1)
        basic.pause(500)
        while (FlameVal != 1) {
            led.stopAnimation()
            basic.showString("RUN")
        }
    }
})
