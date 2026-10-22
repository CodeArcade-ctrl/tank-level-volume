# Tank Level Volume

**Turn a percentage level sensor into remaining and available volume for a tank of known capacity.**

A percentage level reading is hard to act on for rainwater, heating oil, or other storage tanks. This integration converts a percent sensor and configured usable capacity into liters.

## Features

- Remaining volume in liters.
- Empty capacity in liters.
- Reported tank level percentage.

This assumes the selected source is already a 0–100% level measurement. It does not infer tank shape or convert distance readings.

## Install with HACS

1. In Home Assistant, open **HACS → Integrations**.
2. Add `https://github.com/CodeArcade-ctrl/tank-level-volume` as a custom repository of type **Integration**.
3. Install **Tank Level Volume** and restart Home Assistant.
4. Open **Settings → Devices & services → Add integration** and select **Tank Level Volume**.

The catalog request is pending review. Until it is accepted, users must add this repository as a custom repository.

## Privacy and limitations

All calculations run locally in Home Assistant. The integration reads only the selected entities and makes no external network requests. Inputs must have valid numeric states; derived values are unavailable while source values are unknown or invalid.

## License

MIT. See [LICENSE](LICENSE).
