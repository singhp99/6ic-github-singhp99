# Themo Stat Function Tutorial

This is a tutorial of how the `thermo stat` function can be used to check the status of a thermostat depending on the current and desired temperature. Below lies an example of how to use this function. 

## Getting Started 

First we begin by creating a python file `test_func.py` and within it, you can begin by copying the following code:


```ruby
    def my_thermo_stat(temp: int | float, desired_temp: int | float) -> str: 

        if temp < desired_temp - 5:
            status = 'Heat'
        elif temp > desired_temp + 5:
            status = 'AC'
        else:
            status = 'off'
        return status
```

Then, we can check if this code runs by calling the function with the following test inputs 

Input:

```
my_thermo_stat(25,25)
my_thermo_stat(25,19)
my_thermo_stat(15,22)
```

Output:

```
'off'
'AC'
'Heat'
```

For consistency with these tests, it is important to copy the function exactly as outlined above. This function only intended to provide the status of the thermostat to reach the desired temperature, and does not perform any additional action. 

