# opsdroid skill weather

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

Opsdroid will tell you what's forecasted for today, how many degrees and percentage of humidity.

> user: how's the weather outside
>
> opsdroid: It's currently 18.63 degrees, 60% humidity in London and Clouds is forecasted for today

_Note: You can also use the command  `what's the weather`._ 

#### Is it hot/cold
Opsdroid will tell you if you need to take a jacket with you 

> user: is it cold today
>
> opsdroid: It's pretty hot today, it's currently 26.21 degrees outside

_Note: You can also ask if it's `hot` or `nice outside`._

## License

GNU General Public License Version 3 (GPLv3)
