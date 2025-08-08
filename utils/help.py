import re
from collections import Counter
from pathlib import Path

text1 = """
            <site site="DELT1_DELT1-P1" />
            <site site="DELT1_DELT1-P2"/>
            <geom geom="DELT1hh_ellipsoid_DELT1" sidesite="DELT1hh_ellipsoid_DELT1_2_sidesite"/>
            <site site="DELT1_DELT1-P3"/>
            <site site="DELT1_DELT1-P4"/>
            <site site="DELT2_DELT2-P1"/>
            <geom geom="delt2hum_cylinder" sidesite="delt2hum_cylinder_DELT2_1_sidesite"/>
            <site site="DELT2_DELT2-P2"/>
            <geom geom="Deltoid2_ellipsoid_DELT2" sidesite="Deltoid2_ellipsoid_DELT2_2_sidesite"/>
            <site site="DELT2_DELT2-P3"/>
            <site site="DELT2_DELT2-P4"/>
            <site site="DELT3_DELT3-P1"/>
            <geom geom="Delt3_torus" sidesite="Delt3_torus_DELT3_1_sidesite"/>
            <site site="DELT3_DELT3-P2"/>
            <geom geom="delt3hum_ellipsoid_DELT3" sidesite="delt3hum_ellipsoid_DELT3_2_sidesite"/>
            <site site="DELT3_DELT3-P3"/>
            <site site="SUPSP_SUPSP-P1"/>
            <geom geom="SUPSP_ellipsoid_SUPSP" sidesite="SUPSP_ellipsoid_SUPSP_1_sidesite"/>
            <site site="SUPSP_SUPSP-P2"/>
            <site site="SUPSP_SUPSP-P3"/>
            <site site="INFSP_INFSP-P1"/>
            <geom geom="infsp_new_cylinder" sidesite="infsp_new_sidesite"/>
            <site site="INFSP_INFSP-P2"/>
            <site site="INFSP_INFSP-P3"/>
            <site site="SUBSC_SUBSC-P1"/>
            <geom geom="SUBSCAP_ellipsoid_SUBSC" sidesite="SUBSCAP_ellipsoid_SUBSC_1_sidesite"/>
            <site site="SUBSC_SUBSC-P2"/>
            <site site="SUBSC_SUBSC-P3"/>
            <site site="CORB_CORB-P1"/>
            <site site="CORB_CORB-P2"/>
            <site site="CORB_CORB-P3"/>
            <site site="TRIlong_TRIlong-P1"/>
            <geom geom="TRIlonghh_ellipsoid_TRIlong" />
            <site site="TRIlong_TRIlong-P1b" />
            <site site="TRIlong_TRIlong-P2"/>
            <site site="TRIlong_TRIlong-P3"/>
            <site site="TRIlong_TRIlong-P4"/>
            <geom geom="TRI_cylinder" sidesite="TRI_cylinder_TRIlong_4_sidesite"/>
            <site site="TRIlong_TRIlong-P5"/>
            <site site="TRIlat_TRIlat-P1"/>
            <site site="TRIlat_TRIlat-P2"/>
            <site site="TRIlat_TRIlat-P3"/>
            <site site="TRIlat_TRIlat-P4"/>
            <geom geom="TRI_cylinder" sidesite="TRI_cylinder_TRIlat_4_sidesite"/>
            <site site="TRIlat_TRIlat-P5"/>
            <site site="TRImed_TRImed-P1"/>
            <site site="TRImed_TRImed-P2"/>
            <site site="TRImed_TRImed-P3"/>
            <site site="TRImed_TRImed-P4"/>
            <geom geom="TRI_cylinder" sidesite="TRI_cylinder_TRImed_4_sidesite"/>
            <site site="TRImed_TRImed-P5"/>
            <site site="ANC_ANC-P1"/>
            <geom geom="ANC_ellipsoid_ANC" sidesite="ANC_ellipsoid_ANC_1_sidesite" />
            <site site="ANC_ANC-P2"/>
            <site site="SUP_SUP-P1"/>
            <site site="SUP_SUP-P2"/>
            <geom geom="SUP_cylinder" sidesite="SUP_cylinder_SUP_2_sidesite"/>
            <site site="SUP_SUP-P3"/>
            <site site="BIClong_BIClong-P1"/>
            <site site="BIClong_BIClong-P2"/>
            <geom geom="BIClong_ellipsoid_BIClong" sidesite="BIClong_ellipsoid_BIClong_2_sidesite"/>
            <site site="BIClong_BIClong-P3"/>
            <site site="BIClong_BIClong-P4"/>
            <site site="BIClong_BIClong-P5"/>
            <site site="BIClong_BIClong-P6"/>
            <site site="BIClong_BIClong-P7"/>
            <site site="BIClong_BIClong-P8"/>
            <geom geom="Elbow_BIC_BRD_ellipsoid_BIClong" sidesite="Elbow_BIC_BRD_ellipsoid_BIClong_7_sidesite"/>
            <site site="BIClong_BIClong-P10"/>
            <site site="BIClong_BIClong-P11"/>
            <site site="BICshort_BICshort-P1"/>
            <site site="BICshort_BICshort-P2"/>
            <site site="BICshort_BICshort-P3"/>
            <site site="BICshort_BICshort-P4"/>
            <site site="BICshort_BICshort-P5"/>
            <geom geom="Elbow_BIC_BRD_ellipsoid_BICshort" sidesite="Elbow_BIC_BRD_ellipsoid_BICshort_5_sidesite"/>
            <site site="BICshort_BICshort-P6"/>
            <site site="BICshort_BICshort-P7"/>
            <site site="BRA_BRA-P1"/>
            <geom geom="TRI_cylinder" sidesite="TRI_site_BRA_side"></geom>
            <site site="BRA_BRA-P4"/>
            <site site="BRD_BRD-P1"/>
            <geom geom="ElbowBICBRD_ellipsoid_wrap" sidesite="Elbow_BIC_BRD_ellipsoid_BICshort_5_sidesite"/>
            <site site="BRD_BRD-P2"/>
            <site site="BRD_BRD-P3"/>
            <site site="ECRL-P1"/>
            <geom geom="Elbow_PT_ECRL_wrap" sidesite="Elbow_PT_ECRL_site_ECRL_side"></geom>
            <site site="ECRL-P2"/>
            <site site="ECRL-P3"/>
            <geom geom="ECRL_torus_wrap" sidesite="ECRL_torus_site_ECRL_side"/>
            <site site="ECRL-P4"/>
            <site site="ECRB-P1"/>
            <site site="ECRB-P2"/>
            <site site="ECRB-P3"/>
            <geom geom="ECRB_torus_wrap" sidesite="ECRB_torus_site_ECRB_side"/>
            <site site="ECRB-P4"/>
            <site site="ECU-P1"/>
            <site site="ECU-P2"/>
            <site site="ECU-P3"/>
            <site site="ECU-P4"/>
            <site site="ECU-P5"/>
            <geom geom="ECU_torus_wrap" sidesite="ECU_torus_site_ECU_side"/>
            <site site="ECU-P6"/>
            <site site="FCR-P1"/>
            <geom geom="Elbow_PT_FCU_wrap" sidesite="Elbow_PT_FCU_site_FCU_side"></geom>
            <site site="FCR-P2"/>
            <geom geom="FCR_torus_wrap" sidesite="FCR_torus_site_FCR_side"/>
            <site site="FCR-P3"/>
            <site site="FCU-P1"/>
            <geom geom="Elbow_PT_FCU_wrap" sidesite="Elbow_PT_FCU_site_FCU_side"></geom>
            <site site="FCU-P2"/>
            <site site="FCU-P3"/>
            <!-- <geom geom="FCU_torus_wrap" sidesite="FCU_torus_site_FCU_side"/> -->
            <site site="FCU-P4"/>
            <site site="FCU-P5"/>
            <site site="PL-P1"/>
            <geom geom="Elbow_PT_FCU_wrap" sidesite="Elbow_PT_FCU_site_FCU_side"></geom>
            <site site="PL-P2"/>
            <!-- <geom geom="PL_ellipsoid_wrap" sidesite="PL_ellipsoid_site_PL_side"/> -->
            <site site="PL-P3"/>
            <site site="PL-P4"/>
            <site site="PT-P1"/>
            <geom geom="Elbow_PT_FCU_wrap" sidesite="Elbow_PT_FCU_site_FCU_side"></geom>
            <site site="PT-P2"/>
            <site site="PT-P3"/>
            <site site="PT-P4"/>
            <site site="PT-P5"/>
            <site site="PQ-P1"/>
            <geom geom="PQ2_wrap" sidesite="PQ2_site_PQ_side"/>
            <site site="PQ-P2"/>
"""

site_names = re.findall(r'<site site="([^"]+)"', text1)

# Count the occurrences of each site name
site_counts = Counter(site_names)

# Find duplicates (those with count > 1)
duplicates = {site: count for site, count in site_counts.items() if count > 1}

# Print the duplicates
if duplicates:
    print("Found duplicates:")
    for site, count in duplicates.items():
        print(f"{site}: {count} times")
else:
    print("No duplicates found.")



text2 = """

        <site name="DELT1_DELT1-P4" pos="-0.014 0.01106 0.08021" group = '5'/>
        <site name="PECM1_PECM1-P3" pos="0.0264476 0.004005 0.057232"/>
        <site name="PECM1_PECM1-P4" pos="0.00321 -0.00013 0.05113"/>
        <site class="marker" name="R.Clavicle_marker" pos="0.01835 -0.00464 -0.00046"/>


                <site name="Deltoid2_sidesite" pos="-0.006523 -0.02881 0.04238"/>
                <site name="Delt3_sidesite" pos="-0.0973 -0.0428 -0.037"/>
                <site name="INFSP_sidesite" pos="-0.0561 -0.0199 -0.0112"/>
                <site name="TMIN_sidesite" pos="-0.0475 -0.03803 -0.008771"/>
                <site name="TRIlongglen_sidesite" pos="-0.03881 -0.02953 -0.01083"/>
                <site name="s_glenohum_s_glenohum-P2" pos="-0.016 -0.023 -0.017"/>
                <site name="m_glenohum_m_glenohum-P2" pos="-0.014 -0.03 -0.019"/>
                <site name="i_glenohum_i_glenohum-P2" pos="-0.02 -0.036 -0.02"/>
                <site name="coracohum_coracohum-P2" pos="-0.006 -0.026 -0.025"/>
                <site name="DELT1_DELT1-P3" pos="0.04347 -0.03202 0.00499" group="5"/>
                <site name="DELT2_DELT2-P3" pos="5e-05 0.00294 0.02233" group="5"/>
                <site name="DELT2_DELT2-P4" pos="-0.01078 -0.00034 0.0062" group="5"/>
                <site name="Deltoid2_ellipsoid_DELT2_2_sidesite" pos="-0.0403233 -0.0328863 0.017157"/>
                <site name="DELT3_DELT3-P1" pos="-0.05573 0.00122 -0.02512" group="5"/>
                <site name="DELT3_DELT3-P2" pos="-0.07247 -0.03285 0.01233" group="5"/>
                <site name="Delt3_torus_DELT3_1_sidesite" pos="0.3027 0.3572 0.363" group="5"/>
                <site name="SUPSP_SUPSP-P2" pos="-0.0071293297535122493 0.0061517049319610526 0.011581990794449191" group="5"/>
                <site name="SUPSP_SUPSP-P3" pos="-0.044 -0.01512 -0.05855" group="5"/>
                <site name="INFSP_INFSP-P2" pos="-0.0477596 -0.0399154 -0.00963954"/>
                <site name="INFSP_INFSP-P3" pos="-0.07382 -0.05476 -0.04781"/>
                <site name="SUBSC_SUBSC-P2" pos="-0.01831 -0.05223 -0.02457"/>
                <site name="SUBSC_SUBSC-P3" pos="-0.07246 -0.03943 -0.06475"/>
                <site name="TMIN_TMIN-P2" pos="-0.09473 -0.07991 -0.04737"/>
                <site name="TMIN_TMIN-P3" pos="-0.09643 -0.08121 -0.05298"/>
                <site name="TMAJ_TMAJ-P3" pos="-0.09541 -0.109088 -0.0504081"/>
                <site name="TMAJ_TMAJ-P4" pos="-0.106617 -0.11056 -0.0757051"/>
                <site name="LAT1_LAT1-P3" pos="-0.0812616 -0.0723763 -0.0276194"/>
                <site name="LAT2_LAT2-P3" pos="-0.0886248 -0.0793882 -0.0268122"/>
                <site name="LAT3_LAT3-P3" pos="-0.0905824 -0.107059 -0.034711"/>
                <site name="CORB_CORB-P1" pos="0.0125 -0.04127 -0.02652"/>
                <site name="CORB_CORB-P2" pos="0.00483 -0.06958 -0.01563"/>
                <site name="TRIlong_TRIlong-P1" pos="-0.04565 -0.04073 -0.01377"/>
                <site name="BIClong_BIClong-P1" pos="-0.03123 -0.02353 -0.01305"/>
                <site name="BIClong_BIClong-P2" pos="-0.02094 -0.01309 -0.00461"/>
                <site name="BICshort_BICshort-P1" pos="0.01268 -0.03931 -0.02625"/>
                <site name="BICshort_BICshort-P2" pos="0.00093 -0.06704 -0.01593"/>
                <site class="marker" name="R.Shoulder_marker" pos="0.0014 -0.00147 0.01369"/>
                
                                <site name="Elbow_PT_ECRL_site_ECRL_side" pos="0.03 -0.2872 0.04"/>
                                <site name="Elbow_PT_FCU_site_FCU_side" pos="0.03 -0.2872 -0.04"/>

                                <site name="ECRL-P1" pos="-0.0073 -0.2609 0.0091"/>
                                <site name="ECRB-P1" pos="0.0135 -0.2905 0.017"/>
                                <site name="ECU-P1" pos="0.0008 -0.2895 0.0188"/>
                                <site name="FCR-P1" pos="0.0076 -0.2781 -0.037"/>
                                <site name="FCU-P1" pos="0.0022 -0.2774 -0.0388"/>
                                <site name="PL-P1" pos="0.0046 -0.2752 -0.0386"/>
                                <site name="PT-P1" pos="0.0036 -0.2759 -0.0365"/>
                                <site name="FDS5-P1" pos="0.0042 -0.276 -0.0386"/>
                                <site name="FDS4-P1" pos="0.0048 -0.2788 -0.0373"/>
                                <site name="EDC5-P1" pos="-0.0004 -0.2883 0.0187"/>
                                <site name="EDC4-P1" pos="-0.0016 -0.2894 0.0178"/>
                                <site name="EDC3-P1" pos="0.0005 -0.2898 0.0195"/>
                                <site name="EDC2-P1" pos="0.0006 -0.289 0.0187"/>
                                <site name="EDM-P1" pos="0.0009 -0.2892 0.0185"/>

                                <site name="DELT1hh_sidesite" pos="0.01226 -0.01367 -0.009599"/>
                                <site name="delt3hum_sidesite" pos="-0.008209 -0.05929 -0.003236"/>
                                <site name="infsp_new_sidesite" pos="-0.02012 0.02083 0.01693" rgba="1 0 0 0"/>
                                <site name="TMINhum_sidesite" pos="-0.01993 -0.02619 -0.0003194"/>
                                <site name="TMAJ_LAThum_sidesite" pos="-0.0005448 -0.04449 -0.0134"/>
                                <site name="PEC12hum_sidesite" pos="0.007993 -0.05136 -0.009686"/>
                                <site name="PEC1hh_sidesite" pos="0.002716 -0.01113 -0.01877"/>
                                <site name="PEC3hum_sidesite" pos="0.002519 -0.05634 -0.009166"/>
                                <site name="LAT_TMAJhh_sidesite" pos="-0.02747 0.004271 0.01117"/>
                                <site name="Elbow_BIC_BRD_sidesite" pos="0.01774 -0.2888 -0.01624"/>
                                <site name="TRIlonghh_sidesite" pos="-0.02362 -0.006026 -0.01507"/>
                                <site name="ANC_sidesite" pos="0.00314 -0.3043 -0.002981"/>
                                <site name="BIClong_sidesite" pos="0.01267 0.02324 0.004834"/>
                                <site name="CORBhum_sidesite" pos="0.00844 -0.121 -0.01278"/>
                                <site name="Elbow_PT_ECRL_sidesite" pos="0.01843 -0.2761 -0.006962"/>
                                <site name="s_glenohum_s_glenohum-P1" pos="0.018 0.011 -0.009"/>
                                <site name="LIGhh_s_ellipsoid_s_glenohum_1_sidesite" pos="0.00985 0.011 -0.01467"/>
                                <site name="m_glenohum_m_glenohum-P1" pos="0.016 0.003 -0.012"/>
                                <site name="LIGhh_mi_ellipsoid_m_glenohum_1_sidesite" pos="0.01146 0.003222 -0.01556"/>
                                <site name="i_glenohum_i_glenohum-P1" pos="0.009 -0.003 -0.018"/>
                                <site name="LIGhh_mi_ellipsoid_i_glenohum_1_sidesite" pos="0.009 -0.003 -0.018"/>
                                <site name="coracohum_coracohum-P1" pos="0.02 0.011 -0.003"/>
                                <site name="LIGhh_s_ellipsoid_coracohum_1_sidesite" pos="0.01817 0.01067 -0.006444"/>
                                <site name="DELT1_DELT1-P1" pos="0.00896 -0.11883 0.00585" group='5'/>
                                <site name="DELT1_DELT1-P2" pos="0.01623 -0.1033 -0.00412" group = '5' />
                                <site name="DELT1hh_ellipsoid_DELT1_2_sidesite" pos="0.000809535 -0.0383736 -0.00627703" group="5"/>
                                <site name="DELT2_DELT2-P1" pos="0.00461 -0.13611 0.0056" group="5"/>
                                <site name="DELT2_DELT2-P2" pos="0.00623159 -0.0641952 -0.0301843" group="5"/>
                                <site name="delt2hum_cylinder_DELT2_1_sidesite" pos="0.1107 0.0132 0.1101"/>
                                <site name="DELT3_DELT3-P3" pos="0.00206 -0.07602 0.01045" group="5"/>
                                <site name="delt3hum_ellipsoid_DELT3_2_sidesite" pos="0.0108133 -0.0711671 0.00262982"/>
                                <site name="SUPSP_SUPSP-P1" pos="0.00256 0.01063 0.02593" group = "5"/>
                                <site name="SUPSP_ellipsoid_SUPSP_1_sidesite" pos="0.00229806 0.00847163 0.0284548"/>
                                <site name="INFSP_INFSP-P1" pos="-0.00887 0.00484 0.02448"/>
                                <site name="infsp_new_cylinder_INFSP_1_sidesite" pos="-0.0432342 -0.0560158 0.0141316" />-
                                <site name="SUBSC_SUBSC-P1" pos="0.01403 0.0084 -0.01331"/>
                                <site name="SUBSCAP_ellipsoid_SUBSC_1_sidesite" pos="0.0144482 0.0109872 -0.0101213"/>
                                <site name="TMIN_TMIN-P1" pos="-0.00127 -0.01259 0.022"/>
                                <site name="INFSP_and_TMIN_hum_head_ellipsoid_TMIN_1_sidesite" pos="-0.00813624 -0.010913 0.1" rgba="1 0 0 0"/>
                                <site name="TMAJ_TMAJ-P1" pos="0.00998 -0.05419 -0.00568"/>
                                <site name="TMAJ_TMAJ-P2" pos="-0.00625597 -0.049991 -0.0159345"/>
                                <site name="LAT_TMAJ2hh_sphere_TMAJ_2_sidesite" pos="-0.0129153 -0.0208485 -0.0110803"/>
                                <site name="TMAJ_LAThum_cylinder_TMAJ_1_sidesite" pos="0.0707 0.0257 0.0645"/>
                                <site name="PECM1_PECM1-P1" pos="0.01169 -0.04191 0.0078"/>
                                <site name="PECM1_PECM1-P2" pos="0.0210522 -0.01996 0.00793506"/>
                                <site name="PEC1hh_ellipsoid_PECM1_2_sidesite" pos="0.00259407 -0.0252892 -0.00394296" rgba="1 0 0 0"/>
                                <site name="PECM2_PECM2-P1" pos="0.01274 -0.04289 0.00785"/>
                                <site name="PECM2_PECM2-P2" pos="0.0205641 -0.0398321 0.000623549"/><!--
                                <site name="TMAJ_LAT_PEC_CORBhh_sphere_PECM2_2_sidesite" pos="0.0510248 -0.016092 -0.0573453" rgba="1 0 0 5"/>-->
                                <site name="PEC12hum_cylinder_PECM2_1_sidesite" pos="0.092 0.0392 0.0883" rgba="1 0 0 0"/>
                                <site name="PECM3_PECM3-P1" pos="0.01269 -0.04375 0.0075"/>
                                <site name="PECM3_PECM3-P2" pos="0.0159398 -0.0451044 -0.0042896"/>
                                <site name="PEC23hh_sphere_PECM3_2_sidesite" pos="0.0033563 -0.0186528 0.00113941" rgba="1 0 0 0"/>
                                <site name="LAT1_LAT1-P1" pos="0.0105 -0.03415 -0.00653"/>
                                <site name="LAT1_LAT1-P2" pos="-0.00550867 -0.0262692 -0.0129871"/>
                                <site name="LAT_TMAJ2hh_sphere_LAT1_2_sidesite" pos="-0.01849985 -0.0389514 -0.024259" />
                                <site name="TMAJ_LAThum_cylinder_LAT1_1_sidesite" pos="-0.0107 -0.0257 0.0645" />
                                <site name="LAT2_LAT2-P1" pos="0.00968 -0.04071 -0.00611"/>
                                <site name="LAT2_LAT2-P2" pos="-0.00769792 -0.0421159 -0.0156065"/>
                                <site name="LAT_TMAJ2hh_sphere_LAT2_2_sidesite" pos="-0.0157083 -0.017011 -0.0250469" rgba="1 0 0 0"/>
                                <site name="TMAJ_LAThum_cylinder_LAT2_1_sidesite" pos="0.0707 0.0257 0.0645"/>
                                <site name="LAT3_LAT3-P1" pos="0.01208 -0.03922 -0.00416"/>
                                <site name="LAT3_LAT3-P2" pos="-0.0116777 -0.0435673 -0.0143472"/>
                                <site name="LAT_TMAJ2hh_sphere_LAT3_2_sidesite" pos="-0.014069 -0.0219399 -0.00787017"/>
                                <site name="TMAJ_LAThum_cylinder_LAT3_1_sidesite" pos="0.0707 0.0257 0.0645"/>
                                <site name="CORB_CORB-P3" pos="0.00743 -0.15048 -0.00782"/>
                                <site name="CORBhum_cylinder_CORB_2_sidesite" pos="-0.00868897 -0.144208 -0.00172395"/>
                                <site name="TMAJ_LAT_PEC_CORBhh_sphere_CORB_1_sidesite" pos="0.001864 -0.01985 -0.03068" rgba="1 0 0 0"/>
                                <site name="TRIlong_TRIlong-P2" pos="-0.02714 -0.11441 -0.00664"/>
                                <site name="TRIlong_TRIlong-P3" pos="-0.03184 -0.22637 -0.01217"/>
                                <site name="TRIlong_TRIlong-P4" pos="-0.01743 -0.26757 -0.01208"/>
                                <site name="TRI_cylinder_TRIlong_4_sidesite" pos="-0.0156503 -0.293711 0.0175748" />
                                <site name="TRIlonghh_ellipsoid_TRIlong_1_sidesite" pos="-0.0361 -0.00673 0.02277" />
                                <site name="TRIlong_TRIlong-P1b" pos="-0.0365 -0.0044 -0.0213" />
                                <site name="TRIlat_TRIlat-P1" pos="-0.00599 -0.12646 0.00428"/>
                                <site name="TRIlat_TRIlat-P2" pos="-0.02344 -0.14528 0.00928"/>
                                <site name="TRIlat_TRIlat-P3" pos="-0.03184 -0.22637 -0.01217"/>
                                <site name="TRIlat_TRIlat-P4" pos="-0.01743 -0.26757 -0.01208"/>
                                <site name="TRI_cylinder_TRIlat_4_sidesite" pos="-0.0166674 -0.285448 0.0308421"/>
                                <site name="TRImed_TRImed-P1" pos="-0.00838 -0.13695 -0.00906"/>
                                <site name="TRImed_TRImed-P2" pos="-0.02601 -0.15139 -0.0108"/>
                                <site name="TRImed_TRImed-P3" pos="-0.03184 -0.22637 -0.01217"/>
                                <site name="TRImed_TRImed-P4" pos="-0.01743 -0.26757 -0.01208"/>
                                <site name="TRI_cylinder_TRImed_4_sidesite" pos="-0.00964741 -0.30644 -0.0103312"/>
                                <site name="ANC_ANC-P1" pos="-0.00744 -0.28359 0.00979"/>
                                <site name="ANC_ellipsoid_ANC_1_sidesite" pos="0.00142561 -0.280967 0.0164332"/>
                                <site name="BIClong_BIClong-P3" pos="0.01921  0.02083 0.00828"/>
                                <site name="BIClong_BIClong-P4" pos="0.02378 -0.00511 0.01201"/>
                                <site name="BIClong_BIClong-P5" pos="0.01345 -0.02827 0.00136"/>
                                <site name="BIClong_BIClong-P6" pos="0.01068 -0.07736 -0.00165"/>
                                <site name="BIClong_BIClong-P7" pos="0.01703 -0.12125 0.00024"/>
                                <site name="BIClong_BIClong-P8" pos="0.0228 -0.1754 -0.0063"/>
                                <site name="Elbow_BIC_BRD_ellipsoid_BIClong_7_sidesite" pos="0.00972896 -0.273869 -0.0199478"/>
                                <site name="BIClong_ellipsoid_BIClong_2_sidesite" pos="0.02337 0.01102 0.001639"/>
                                <site name="BICshort_BICshort-P3" pos="0.01117 -0.07576 -0.01101"/>
                                <site name="BICshort_BICshort-P4" pos="0.01703 -0.12125 -0.01079"/>
                                <site name="BICshort_BICshort-P5" pos="0.0228 -0.1754 -0.0063"/>
                                <site name="Elbow_BIC_BRD_ellipsoid_BICshort_5_sidesite" pos="0.0158403 -0.275971 -0.0182235"/>
                                <site name="BRA_BRA-P1" pos="0.0068 -0.1739 -0.0036"/>
                                <site name="BRD_BRD-P1" pos="-0.0098 -0.19963 0.00223"/>

                                <site name="TRI_site_BRA_side" pos="0.0188814 -0.25991 0.0179386"></site>

                                <site class="marker" name="R.Bicep_marker" pos="0.01591 -0.181 -0.00553"/>
                                <site class="marker" name="R.Elbow.Lateral_marker" pos="0.00509 -0.2806 0.02884"/>
                                <site class="marker" name="R.Elbow.Medial_marker" pos="-0.00407 -0.2844 -0.05408"/>
                               
                               <site name="ECU-P2" pos="-0.0139 -0.032 0.0295"/>
                                    <site name="ECU-P3" pos="-0.017 -0.0543 0.0287"/>
                                    <site name="ECU-P4" pos="-0.0179 -0.0957 0.0328"/>
                                    <site name="PT-P2" pos="0.0085 -0.0337 -0.0143"/>
                                    <site name="PT-P3" pos="0.0122 -0.0652 -0.0022"/>
                                    <site name="PQ-P2" pos="0.0019 -0.2097 0.0363"/>
                                    <site name="FDS3-P1" pos="-0.0067 -0.0271 -0.0019"/>
                                    <site name="FDS2-P1" pos="-0.0068 -0.0282 -0.0014"/>
                                    <site name="FDP5-P1" pos="-0.0063 -0.0321 0.0025"/>
                                    <site name="FDP4-P1" pos="-0.005 -0.0337 0.0027"/>
                                    <site name="FDP3-P1" pos="-0.0052 -0.0333 0.0021"/>
                                    <site name="FDP2-P1" pos="-0.0065 -0.0318 0.0028"/>
                                    <site name="EDM-P2" pos="-0.0098 -0.0391 0.0308"/>
                                    <site name="EDM-P3" pos="-0.0076 -0.0827 0.0365"/>
                                    <site name="EIP-P1" pos="-0.0039 -0.1665 0.0368"/>
                                    <site name="EIP-P2" pos="0.0017 -0.1747 0.0405"/>
                                    <site name="EPL-P1" pos="-0.0141 -0.0971 0.0295"/>
                                    <site name="PQ2_site_PQ_side" pos="-0.0012 -0.2092 0.0428"/>
                                    <site name="TRIlong_TRIlong-P5" pos="-0.0219 0.01046 -0.00078"/>
                                    <site name="TRIlat_TRIlat-P5" pos="-0.0219 0.01046 -0.00078"/>
                                    <site name="TRImed_TRImed-P5" pos="-0.0219 0.01046 -0.00078"/>
                                    <site name="ANC_ANC-P2" pos="-0.02532 -0.00124 0.006"/>
                                    <site name="SUP_SUP-P3" pos="-0.0136 -0.03384 0.02013"/>
                                    <site name="BRA_BRA-P4" pos="-0.0032 -0.0239 0.0009"/>
                                    <site class="marker" name="R.Ulna_marker" pos="-0.01672 -0.2416 0.04782"/>
                                   
                                   
                                   <site name="ECRL-P2" pos="0.032 -0.1346 0.0278"/>
                                        <site name="ECRL-P3" pos="0.0424 -0.2368 0.0362"/>
                                        <site name="ECRB-P2" pos="0.029 -0.1309 0.0238"/>
                                        <site name="ECRB-P3" pos="0.0355 -0.228 0.0394"/>
                                        <site name="ECU-P5" pos="-0.0142 -0.227 0.0348"/>
                                        <site name="FCR-P2" pos="0.0211 -0.2194 0.0013"/>
                                        <site name="FCU-P3" pos="0.0108 -0.2233 0.0097"/>
                                        <!-- <site name="FCU-P2" pos="0.0101 -0.1835 0.002"/> -->
                                        <site name="FCU-P2" pos="0.0095 -0.1841 0.0005"></site>
                                        <site name="PL-P2" pos="0.0253 -0.2392 -0.0028"/>
                                        <site name="PT-P5" pos="0.0254 -0.1088 0.0198"/>
                                        <site name="PT-P4" pos="0.0236 -0.0934 0.0094"/>
                                        <site name="PQ-P1" pos="0.0324 -0.2 0.0196"/>
                                        <site name="FDS5-P2" pos="0.0138 -0.1872 0.002"/>
                                        <site name="FDS4-P2" pos="0.0157 -0.1867 0.0027"/>
                                        <site name="FDS3-P2" pos="0.019 -0.1871 0.0042"/>
                                        <site name="FDS2-P2" pos="0.0214 -0.1862 0.0055"/>
                                        <site name="FDP5-P2" pos="0.0141 -0.1852 0.0086"/>
                                        <site name="FDP4-P2" pos="0.0158 -0.1863 0.008"/>
                                        <site name="FDP3-P2" pos="0.0191 -0.1864 0.0078"/>
                                        <site name="FDP2-P2" pos="0.0208 -0.1856 0.0092"/>
                                        <site name="EDC5-P3" pos="0.0099 -0.223 0.0362"/>
                                        <site name="EDC5-P2" pos="0.0013 -0.0383 0.013"/>
                                        <site name="EDC4-P3" pos="0.0088 -0.2237 0.0428"/>
                                        <site name="EDC4-P2" pos="0.0026 -0.0393 0.0144"/>
                                        <site name="EDC3-P3" pos="0.0144 -0.2232 0.0422"/>
                                        <site name="EDC3-P2" pos="0.0032 -0.0389 0.0142"/>
                                        <site name="EDC2-P3" pos="0.0153 -0.2231 0.042"/>
                                        <site name="EDC2-P2" pos="0.0023 -0.0386 0.0137"/>
                                        <site name="EDM-P4" pos="0.0045 -0.2264 0.0368"/>
                                        <site name="EIP-P3" pos="0.0108 -0.2278 0.0366"/>
                                        <site name="EPL-P2" pos="0.0012 -0.1367 0.0227"/>
                                        <site name="EPL-P3" pos="0.027 -0.2187 0.0383"/>
                                        <site name="EPL-P4" pos="0.0338 -0.2275 0.0461"/>
                                        <site name="EPL-P5" pos="0.0423 -0.2377 0.0417"/>
                                        <site name="EPB-P1" pos="0.0192 -0.147 0.0211"/>
                                        <site name="EPB-P2" pos="0.0228 -0.1586 0.0266"/>
                                        <site name="EPB-P3" pos="0.0383 -0.1972 0.0383"/>
                                        <site name="EPB-P4" pos="0.0524 -0.2361 0.027"/>
                                        <site name="FPL-P1" pos="0.0097 -0.0946 0.0177"/>
                                        <site name="FPL-P2" pos="0.0166 -0.1352 0.0192"/>
                                        <site name="FPL-P3" pos="0.0187 -0.1793 0.0199"/>
                                        <site name="FPL-P4" pos="0.038 -0.2317 0.0158"/>
                                        <site name="APL-P1" pos="0.0115 -0.0948 0.0168"/>
                                        <site name="APL-P2" pos="0.0303 -0.1397 0.0351"/>
                                        <site name="APL-P3" pos="0.0399 -0.1607 0.034"/>
                                        <site name="APL-P4" pos="0.044 -0.1784 0.0313"/>
                                        <site name="APL-P5" pos="0.055 -0.2308 0.0237"/>
                                        <site name="ECU_torus_site_ECU_side" pos="-0.0163 -0.2417 0.0349"/>

                                        <site name="SUP_sidesite" pos="0.01106 -0.04094 0.01141"/>
                                        <site name="ECU_sidesite" pos="-0.0163 -0.2417 0.0349"/>
                                        <site name="SUP_SUP-P1" pos="0.00996 -0.06096 0.00075"/>
                                        <site name="SUP_SUP-P2" pos="0.01201 -0.0517 -0.00107"/>
                                        <site name="SUP_cylinder_SUP_2_sidesite" pos="0.00511946 -0.043905 0.0155965"/>
                                        <site name="BIClong_BIClong-P10" pos="-0.00670279 -0.0291637 -0.0127257"/>
                                        <site name="BIClong_BIClong-P11" pos="-0.002 -0.0375 -0.002"/>
                                        <site name="BICshort_BICshort-P6" pos="-0.00774281 -0.0255585 -0.0131094"/>
                                        <site name="BICshort_BICshort-P7" pos="-0.002 -0.0375 -0.002"/>
                                        <site name="BRD_BRD-P2" pos="0.03577 -0.12742 0.02315"/>
                                        <site name="BRD_BRD-P3" pos="0.0419 -0.221 0.0224"/>
                                        <site class="marker" name="R.Forearm_marker" pos="0.03828 -0.1133 0.0174"/>
                                        <site class="marker" name="R.Radius_marker" pos="0.05749 -0.2272 0.02738"/>

"""





import re
from collections import Counter

# Extract from text1
site_names1 = re.findall(r'<site site="([^"]+)"', text1)
site_counts1 = Counter(site_names1)
duplicates1 = {site: count for site, count in site_counts1.items() if count > 1}

# Extract from text2
site_names2 = re.findall(r'<site name="([^"]+)"', text2)
site_counts2 = Counter(site_names2)
duplicates2 = {site: count for site, count in site_counts2.items() if count > 1}

# Compare sets
missing_in_text2 = set(site_names1) - set(site_names2)
extra_in_text2 = set(site_names2) - set(site_names1)

# Print results
print("Duplicates in text1:")
for site, count in duplicates1.items():
    print(f"  {site}: {count}")

print("\nDuplicates in text2:")
for site, count in duplicates2.items():
    print(f"  {site}: {count}")

print("\nMissing in text2 (present in text1 but not in text2):")
for site in sorted(missing_in_text2):
    print(f"  {site}")

print("\nExtra in text2 (not in text1):")
for site in sorted(extra_in_text2):
    print(f"  {site}")








allowed_sites = set(re.findall(r'<site\s+site="([^"]+)"', text1))
print(f"Allowed site count (from text1): {len(allowed_sites)}")

def remove_extra_sites(fragment: str, allowed: set) -> (str, list):
    """
    Remove <site ...> elements from fragment where the name attribute isn't in allowed.
    Keeps everything else intact. Returns cleaned text and list of removed names (may contain duplicates).
    """
    out_parts = []
    idx = 0
    removed = []
    total_found = 0
    while True:
        m = re.search(r'<site\b', fragment[idx:])
        if not m:
            out_parts.append(fragment[idx:])
            break
        start = idx + m.start()
        # append leading text up to the <site
        out_parts.append(fragment[idx:start])
        # find end of the start tag
        gt = fragment.find('>', start)
        if gt == -1:
            # malformed - no closing '>' found, append rest and break
            out_parts.append(fragment[start:])
            break
        start_tag = fragment[start:gt+1]
        # find name attribute in start_tag
        name_match = re.search(r'\bname\s*=\s*"(.*?)"', start_tag)
        if name_match:
            name = name_match.group(1)
            total_found += 1
        else:
            # No name attribute: keep the whole start tag and continue
            # Determine if self-closing or not
            if start_tag.rstrip().endswith('/>'):
                out_parts.append(start_tag)
                idx = gt + 1
                continue
            # find closing </site>
            close = fragment.find('</site>', gt+1)
            if close == -1:
                out_parts.append(start_tag)
                idx = gt + 1
                continue
            full = fragment[start:close+7]
            out_parts.append(full)
            idx = close + 7
            continue

        # If start tag is self-closing (ends with '/>'), treat as single piece
        if start_tag.rstrip().endswith('/>'):
            full_tag = start_tag
            if name in allowed:
                out_parts.append(full_tag)
            else:
                removed.append(name)
            idx = gt + 1
            continue
        else:
            # Not self-closing: find matching </site>
            close = fragment.find('</site>', gt+1)
            if close == -1:
                # No closing tag found — keep the start_tag and move on
                if name in allowed:
                    out_parts.append(start_tag)
                else:
                    removed.append(name)
                idx = gt + 1
                continue
            full_tag = fragment[start:close+7]  # include '</site>'
            if name in allowed:
                out_parts.append(full_tag)
            else:
                removed.append(name)
            idx = close + 7
            continue

    cleaned = ''.join(out_parts)
    return cleaned, removed, total_found

text3, removed_names, total_sites_in_text2 = remove_extra_sites(text2, allowed_sites)

print(f"Total <site ...> occurrences with name found in text2 scanned: {total_sites_in_text2}")
print(f"Removed {len(removed_names)} site entries (names not present in text1).")
if removed_names:
    # show unique removed names (limited to first 200 names if many)
    unique_removed = list(dict.fromkeys(removed_names))
    print("Some removed names (unique):", unique_removed[:200])

# Save text3
out_path = Path("text3.xml")
out_path.write_text(text3, encoding="utf-8")

# Print a short preview and full length
print("\n--- BEGIN text3 preview (first 2000 chars) ---\n")
print(text3[:2000])
print("\n--- END preview ---\n")
print(f"text3 saved to: {out_path} (length {len(text3)} characters)")

# Also show a small summary of differences
kept_names = set(re.findall(r'<site\b[^>]*\bname="([^"]+)"', text3))
print(f"Kept site count in text3: {len(kept_names)}")

# Print a small diff-like summary: names that were in text2 but removed
names_in_text2 = set(re.findall(r'<site\b[^>]*\bname="([^"]+)"', text2))
extra_in_text2 = names_in_text2 - allowed_sites
print(f"Extra in text2 (not in text1): {len(extra_in_text2)} names. Example: {list(extra_in_text2)[:20]}")

# For user's convenience, also print the full removed names if not too many
if len(unique_removed) <= 200:
    print("\nFull list of removed names:")
    print('\\n'.join(unique_removed))

# Provide the file path for download
print(f"\nYou can download the cleaned file at: sandbox:/mnt/data/text3.xml")