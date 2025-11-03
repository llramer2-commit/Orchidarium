## allow script to sleep between readings
import time
import argparse

## talk and interact with DHT22 sensor
import adafruit_dht
import board


def parse_args():
    parser = argparse.ArgumentParser(
        description="Read temperature and humidity from a DHT22 sensor using a board pin"
    )
    parser.add_argument(
        "-p",
        "--pin",
        default="D4",
        help="Board pin attribute name from the board module (e.g., D4, D17). Default: D4",
    )
    return parser.parse_args()


def resolve_pin(pin_name: str):
    """Return the pin object from the board module for the given attribute name.

    Raises ValueError if the attribute does not exist.
    """
    try:
        return getattr(board, pin_name)
    except AttributeError:
        raise ValueError(f"Pin '{pin_name}' not found in board module")


def main():
    args = parse_args()

    try:
        pin = resolve_pin(args.pin)
    except ValueError as e:
        print(e)
        return 2

    dht_device = adafruit_dht.DHT22(pin)

    try:
        # Get readings from sensor constantly
        while True:
            try:
                temperature_c = dht_device.temperature
                temperature_f = temperature_c * (9 / 5) + 32
                humidity = dht_device.humidity

                print(
                    f"Temp:{temperature_c:.1f} C / {temperature_f:.1f} F  Humidity: {humidity}%"
                )
            except RuntimeError as error:
                # Common transient read errors from the DHT sensor
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception:
                # Ensure sensor is cleaned up on unexpected exceptions
                dht_device.exit()
                raise

            time.sleep(3.0)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        try:
            dht_device.exit()
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main())

