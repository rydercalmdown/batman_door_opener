# Batman Door Opener
A project that lets keys played on my piano accomplish tasks - like opening secret doors in the Batman Movies.

## Installing
To install on a raspberry pi, clone this repository, cd into it, and run the following command:

```
make install-raspberry-pi
```

It will ask you for your password, then install base dependencies, a virtual environment, and python dependencies.

Connect your piano, and test that you can see it under the following command:
```
amiidi -l
```

It should appear as the first or second line (code is configured to take the second line if it exists).

**Note**: This repository should also run on OSX, but it will not be able to run a relay, and you might need to comment out imports to the pneumatics.py file.


## To Run
To run, use the following command:
```
make run
```

## Adding Patterns
To add a pattern, extend the PatternBase class in patterns.py, and implement the following methods:

```python

class YourNewPattern(PatternBase):

    def pattern(self):
        # Define your pattern here (notes can be seen by enabling l.print_notes = True in app.py)
        # these are the notes it will recognize in order.
        return [84, 86, 96, 98, 91, 93]

    def callback(self):
        # Define your callback here - if you're not familiar with a callback, this is where you
        # put the code you want to execute when your pattern occurs
        print('Pattern Recognized')

    def is_active(self):
        # Set this to false if you want to disable the pattern temporarily
        return True

```
