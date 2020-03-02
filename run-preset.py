import os

import click

from devito import configuration, info, norm
from devito.types.dense import DiscreteFunction

from benchmarks.user.benchmark import run_jit_backdoor


@click.command()
@click.argument('problem',
                type=click.Choice(['acoustic', 'tti']))
def cli_run_jit_backdoor(problem, **kwargs):
    """`click` interface for the `run_jit_backdoor` mode in `benchmark.py`."""

    # Preset shared parameters
    kwargs['space_order'] = [12]
    kwargs['time_order'] = [2]
    kwargs['nbl'] = 10
    kwargs['spacing'] = (20.0, 20.0, 20.0)

    # Preset problem-specific parameters
    if problem == 'tti':
        kwargs['shape'] = (350, 350, 350)
        kwargs['tn'] = 50  # End time of the simulation in ms
        kwargs['dse'] = 'aggressive'

        # Reference norms for the output fields
        reference = {'rec': 66.417102, 'u': 30.707737, 'v': 30.707728}
    elif problem == 'acoustic':
        kwargs['shape'] = (492, 492, 492)
        kwargs['tn'] = 100  # End time of the simulation in ms
        kwargs['dse'] = 'advanced'

        # Reference norms for the output fields
        reference = {'rec': 184.526400, 'u': 151.545837}
    else:
        assert False

    # Dummy values as they will be unused
    kwargs['block_shape'] = []
    kwargs['autotune'] = 'off'

    retval = run_jit_backdoor(problem, **kwargs)

    if retval is not None:
        for i in retval:
            if isinstance(i, DiscreteFunction):
                v = norm(i)
                info("norm(%s) = %f (expected = %f, delta = %f)"
                     % (i.name, v, reference[i.name], abs(v - reference[i.name])))

    # Record DEVITO_ environment
    env = [(k, v) for k, v in os.environ.items() if k.startswith('DEVITO_')]
    content = "{%s}" % ", ".join("'%s': '%s'" % (k, v) for k, v in env)
    with open('env.py', 'w') as f:
        f.write(content)


if __name__ == "__main__":
    configuration['profiling'] = 'advanced'

    cli_run_jit_backdoor()
