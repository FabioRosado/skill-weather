# opsdroid skill google it

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to tell you the current weather

## Requirements

You need an api-key from [OpenWeatherMap](https://openweathermap.org/api).

## Configuration

```yaml
skills:
  - name: weather
    # Required
    city: London,UK    # For accuracy use {city},{country code}          
    unit: metric       # Choose metric/imperial
    api-key: 6fut9e098d8g90g
```

## Usage

#### weather

Googles "pomodoro technique".

> user: weather
>
> opsdroid: It's currently 18.63 degrees, 60% humidity in London and Clouds is forecasted for today

## License

GNU General Public License Version 3 (GPLv3)
