# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..preprocess import BBRegister


def test_BBRegister_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    contrast_type=dict(argstr='--%s',
    mandatory=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    epi_mask=dict(argstr='--epi-mask',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    init=dict(argstr='--init-%s',
    mandatory=True,
    xor=['init_reg_file'],
    ),
    init_reg_file=dict(argstr='--init-reg %s',
    mandatory=True,
    xor=['init'],
    ),
    intermediate_file=dict(argstr='--int %s',
    ),
    out_fsl_file=dict(argstr='--fslmat %s',
    ),
    out_reg_file=dict(argstr='--reg %s',
    genfile=True,
    ),
    reg_frame=dict(argstr='--frame %d',
    xor=['reg_middle_frame'],
    ),
    reg_middle_frame=dict(argstr='--mid-frame',
    xor=['reg_frame'],
    ),
    registered_file=dict(argstr='--o %s',
    ),
    source_file=dict(argstr='--mov %s',
    copyfile=False,
    mandatory=True,
    ),
    spm_nifti=dict(argstr='--spm-nii',
    ),
    subject_id=dict(argstr='--s %s',
    mandatory=True,
    ),
    subjects_dir=dict(),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = BBRegister.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_BBRegister_outputs():
    output_map = dict(min_cost_file=dict(),
    out_fsl_file=dict(),
    out_reg_file=dict(),
    registered_file=dict(),
    )
    outputs = BBRegister.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
