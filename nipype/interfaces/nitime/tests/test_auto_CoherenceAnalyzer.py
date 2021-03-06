# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..analysis import CoherenceAnalyzer


def test_CoherenceAnalyzer_inputs():
    input_map = dict(NFFT=dict(usedefault=True,
    ),
    TR=dict(),
    figure_type=dict(usedefault=True,
    ),
    frequency_range=dict(usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_TS=dict(),
    in_file=dict(requires=('TR',),
    ),
    n_overlap=dict(usedefault=True,
    ),
    output_csv_file=dict(),
    output_figure_file=dict(),
    )
    inputs = CoherenceAnalyzer.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_CoherenceAnalyzer_outputs():
    output_map = dict(coherence_array=dict(),
    coherence_csv=dict(),
    coherence_fig=dict(),
    timedelay_array=dict(),
    timedelay_csv=dict(),
    timedelay_fig=dict(),
    )
    outputs = CoherenceAnalyzer.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
