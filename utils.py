import time


def timer(operation_name):
    def real_decorator(some_function):
        """
        Outputs the time a function takes to execute.
        """

        def wrapper(self, filename):
            t1 = time.time()
            some_function(self, filename)
            t2 = time.time()
            print(operation_name + " took : " + str((t2 - t1)) + "\n")

        return wrapper

    return real_decorator
