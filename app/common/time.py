def time_wrapper(above_seconds=0.0, callback=None, *outer_args, **outer_kwargs):
    def decorator(function):
        def wrapper(*args, **kwargs):
            import time
            start = time.time()
            result = function(*args, **kwargs)
            end = time.time()
            delta_secs = (end - start)
            if delta_secs >= above_seconds:
                if callback is None:
                    print('{:s} function took {:.3f} ms'.format(function.__name__, delta_secs * 1000.0))
                else:
                    callback(delta_secs, *args)
            return result

        return wrapper

    return decorator


def time_wrapper_old(f):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        ret = f(*args, **kwargs)
        end = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (end - start) * 1000.0))
        return ret

    return wrapper
