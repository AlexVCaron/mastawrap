from mastasupport.logger import logger


def test_logger_decorator(name):
    args = ("fake_arg_1", "fake_arg_2")
    kwargs = {
        "fake_kwarg_1": "fake_kwarg_1",
        "fake_kwarg_2": "fake_kwarg_2",
        "fake_kwarg_3": "fake_kwarg_3"
    }

    @logger(name)
    def fake_function_to_log(f_args, f_kwargs):
        assert_tuples(f_args, args)
        assert_dicts(f_kwargs, kwargs)
        return "result"

    return fake_function_to_log(args, kwargs)


def assert_tuples(f_args, args):
    assert len(f_args) == len(args)
    for i in range(0, len(f_args)):
        assert args[i] is f_args[i] or args[i] == f_args[i]


def assert_dicts(f_kwargs, kwargs):
    assert len(f_kwargs) == len(kwargs)
    for key in f_kwargs:
        assert key in kwargs
        assert kwargs[key] is f_kwargs[key] or kwargs[key] == f_kwargs[key]