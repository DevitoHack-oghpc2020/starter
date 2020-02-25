import click

from devito import configuration, info, norm
from devito.types.dense import DiscreteFunction

from benchmarks.user.benchmark import run_jit_backdoor


@click.command()
@click.argument('problem',
                type=click.Choice(['acoustic', 'tti', 'tti-agg', 'viscoelastic']))
def cli_run_jit_backdoor(problem, **kwargs):
    """`click` interface for the `run_jit_backdoor` mode in `benchmark.py`."""

    # Preset problem parameters, discretization, etc
    kwargs['shape'] = (492, 492, 492)
    kwargs['space_order'] = [12]
    kwargs['time_order'] = [2]
    kwargs['nbl'] = 10
    kwargs['tn'] = 50  # End time of the simulation in ms
    kwargs['spacing'] = (20.0, 20.0, 20.0)

    # Preset performance
    if problem == 'tti-agg':
        problem = 'tti'
        kwargs['dse'] = 'aggressive'
    else:
        kwargs['dse'] = 'advanced'

    # Dummy values as they will be unused
    kwargs['block_shape'] = []
    kwargs['autotune'] = 'off'

    retval = run_jit_backdoor(problem, **kwargs)

    if retval is not None:
        for i in retval:
            if isinstance(i, DiscreteFunction):
                info("norm(%s) = %f" % (i.name, norm(i)))


if __name__ == "__main__":
    configuration['profiling'] = 'advanced'

    cli_run_jit_backdoor()
