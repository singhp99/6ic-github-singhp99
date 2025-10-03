# Themo Stat Function How-to Make Changes

##Changing the Tolerance 
Follow the [tutorial](tutorial_thermo.md) to get the starter function. This is only a very simple starting function, we can stop here if we want but why do so when we can improve it. There are many avenues to altering this function, but let's begin with a simple change that gets us more familiar with this function. 

We can make a small alteration by changing the value of difference required between the two variables `temp` and `desired_temp` by defining a new variable called `tol = 5` and replacing it with the `5` in

```
if temp < desired_temp - 5:
```

and 

```
elif temp > desired_temp + 5:
```
If this variable is set to `tol = 5` and the tests above are rerun, you should get the same exact outcome. But you can set this to any other number now. **Note: instantiate this variable *before* the if statements.**

Though this is a simple change, it allows us to probe the function and learn how we can begin to improve it for a more complex version. You now have the starting function and have made the first change, these are the tools you can use for further development. Good luck!


