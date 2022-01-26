import os

def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    t1w = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_T1w')
    func_rest_AP = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_dir-AP_bold')
    func_rest_PA = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_dir-PA_bold')
    func_ssrt_AP = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-ssrt_dir-AP_bold')
    func_ssrt_PA = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-ssrt_dir-PA_bold')
    func_card_AP = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-card_dir-AP_bold')
    func_card_PA = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-card_dir-PA_bold')
    fmap_fmri_mag = create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-fmri_magnitude')
    fmap_fmri_phase = create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-fmri_phasediff')
    fmap_dwi_mag = create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-dwi_magnitude')
    fmap_dwi_phase = create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-dwi_phasediff')
    dwi_3000 = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-3000_dwi')
    dwi_2000 = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-2000_dwi')
    dwi_1000 = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-1000_dwi')
    loc = create_key('sub-{subject}/{session}/loc/sub-{subject}_{session}_loc')
    b0_AP = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-b0_dir-AP_dwi')
    b0_PA = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-b0_dir-PA_dwi')



    
    info = {t1w: [], func_rest_AP: [], func_rest_PA: [], func_ssrt_AP: [], func_ssrt_PA: [], func_card_AP: [], func_card_PA: [], fmap_fmri_mag: [], fmap_fmri_phase: [], fmap_dwi_mag: [], fmap_dwi_phase: [], dwi_3000: [], dwi_2000: [], dwi_1000: [], loc: [], b0_AP: [], b0_PA: [], dwi_3000: [], dwi_2000: [], dwi_1000: []}
    
    
    for idx, s in enumerate(seqinfo):
        if (s.dim1 == 256) and (s.dim4 == 1) and ('MEMPRAGE' in s.protocol_name):
            info[t1w].append(s.series_id)
        if (s.dim3 == 68) and (s.dim4 == 330) and ('SMS_mb4_2mm_AtoP_Resting' in s.protocol_name):
            info[func_rest_AP].append(s.series_id)
        if (s.dim3 == 68) and (s.dim4 == 330) and ('SMS_mb4_2mm_PtoA_Resting' in s.protocol_name):
            info[func_rest_PA].append(s.series_id)
        if (s.dim1 == 104) and (s.dim3 == 68) and ('SMS_mb4_2mm_AtoP_SSRT' in s.protocol_name):
            info[func_ssrt_AP].append(s.series_id)
        if (s.dim1 == 104) and (s.dim3 == 68) and ('SMS_mb4_2mm_PtoA_SSRT' in s.protocol_name):
            info[func_ssrt_PA].append(s.series_id)
        if (s.dim1 == 104) and (s.dim3 == 68) and ('SMS_mb4_2mm_AtoP_Card' in s.protocol_name):
            info[func_card_AP].append(s.series_id)
        if (s.dim1 == 104) and (s.dim3 == 68) and ('SMS_mb4_2mm_PtoA_Card' in s.protocol_name):
            info[func_card_PA].append(s.series_id)
        if (s.dim1 == 104) and (s.dim3 == 136) and ('gre_field_mapping_2mm_fmri' in s.protocol_name):
            info[fmap_fmri_mag].append(s.series_id)
        if (s.dim1 == 104) and (s.dim3 == 68) and ('gre_field_mapping_2mm_fmri' in s.protocol_name):
            info[fmap_fmri_phase].append(s.series_id)
        if (s.dim1 == 104) and (s.dim3 == 132) and ('gre_field_mapping_2mm_dwi' in s.protocol_name):
            info[fmap_dwi_mag].append(s.series_id)
        if (s.dim1 == 104) and (s.dim3 == 66) and ('gre_field_mapping_2mm_dwi' in s.protocol_name):
            info[fmap_dwi_phase].append(s.series_id)
        if (s.dim1 == 104) and (s.dim4 == 147) and ('ep2d_diff_qspace_p2_s2_3000' in s.protocol_name):
            info[dwi_3000].append(s.series_id)
        if (s.dim1 == 104) and (s.dim4 == 66) and ('ep2d_diff_qspace_p2_s2_2000' in s.protocol_name):
            info[dwi_2000].append(s.series_id)
        if (s.dim1 == 104) and (s.dim4 == 18) and ('ep2d_diff_qspace_p2_s2_1000' in s.protocol_name):
            info[dwi_1000].append(s.series_id)
        if (s.dim1 == 512) and (s.dim4 == 1) and ('localizer' in s.protocol_name):
            info[loc].append(s.series_id)
        if (s.dim1 == 104) and (s.dim4 == 1) and ('AP_B03' in s.protocol_name):
            info[b0_AP].append(s.series_id)
        if (s.dim1 == 104) and (s.dim4 == 1) and ('PA_B03' in s.protocol_name):
            info[b0_PA].append(s.series_id)        
            
    return info
