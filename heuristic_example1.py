import os

# This block of code defines a function called create_key
def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    # Key definitions. Revised for each new study or after modifying the study design.
    ###################################################################
    # Use the create_key function to define a unique variable for each sequence:
    # variable = create_key(output_directory_path_and_name).
    data = create_key('run-{item:d}')
    t1w = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_T1w')
    rest1 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_run-1_sbref')
    rest2 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_run-1_bold')
    rest3 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_run-2_sbref')
    rest4 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_run-2_bold')
    mutiband1 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-msit_run-1_bold')
    mutiband2 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-ssrt_run-1_bold')
    mutiband3 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-ssrt_run-2_bold')
    diff = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_dwi')

    # This data dictionary containing user-defined variables also subject to revision.
    ##########################################################################
    # Enter a key in the dictionary for each key you created above in section 1.
    info = {data: [], t1w: [], rest1: [], rest2: [], rest3: [], rest4: [], mutiband1: [], mutiband2: [], mutiband3: [], diff: []}
    last_run = len(seqinfo)

    # Section 2: These criteria should be revised by user.
    ##########################################################
    # Define test criteria to check that each dicom sequence is classified correctly.
    # seqinfo (s) refers to information in dicominfo.tsv. Consult that file for available criteria.
    # Here we use two types of criteria:
    # 1) An equivalent field "==" (e.g., good for checking dimensions)
    # 2) A field that includes a string (e.g., 'mprage' in s.protocol_name)
    
    for idx, s in enumerate(seqinfo):
        if ('7-T1_MEMPRAGE_1.2mm_p4' in s.series_id):
           info[t1w].append(s.series_id)
        if ('8-SMS_Minn_2p4mm_REST1' in s.series_id):
            info[rest1].append(s.series_id)
        if ('9-SMS_Minn_2p4mm_REST1' in s.series_id):
            info[rest2].append(s.series_id)
        if ('10-SMS_Minn_2p4mm_REST1' in s.series_id):
            info[rest3].append(s.series_id)
        if ('11-SMS_Minn_2p4mm_REST1' in s.series_id):
            info[rest4].append(s.series_id)
        if ('12-mutiband_bold340new' in s.series_id):
            info[mutiband2].append(s.series_id)
        if ('13-mutiband_bold340new' in s.series_id):
            info[mutiband3].append(s.series_id)
        if ('14-mutiband_bold480new' in s.series_id):
            info[mutiband1].append(s.series_id)
        if ('15-cmrr_mbep2d_diff' in s.series_id):
            info[diff].append(s.series_id)
    return info

