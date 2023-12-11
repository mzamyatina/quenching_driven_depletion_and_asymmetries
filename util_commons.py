import iris
from pathlib import Path
from util_mypaths import path_to_data_umserve

PLANETS = {
    "wasp96b": {"tex": "WASP-96b"},
}

ROSE_SUITES = {
    "wasp96b": {
        "common": {
            "planet": "wasp96b",
        },
        "equilibrium": {
            "chemical_scheme": "equilibrium",
            "mdh_0": {
                "mdh": "0",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium mdh=0 dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp96b"
                    / "initial_profile"
                    / "WASP-96b_PT_EQ.ncdf"
                ),
                "star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp96b"
                    / "spectral_files"
                    / "spec_file_wasp96b_mdh0_sw_500"  # spec_file_wasp96b_mdh0_sw_500 spec_file_wasp96b_mdh0_sw_500_2micron
                ),
                "tK_1": {
                    "diff_timescale_wind": "1",
                    "rose_suite": "u-cp158_tK1",
                    "dir_for_data": Path(
                        path_to_data_umserve
                        / "um_runs"
                        / "wasp96b"
                        / "equilibrium"
                        / "u-cp158_tK1"
                    ),
                },
                "tK_6": {
                    "diff_timescale_wind": "6",
                    "rose_suite": "u-cp158_tK6",
                    "dir_for_data": Path(
                        path_to_data_umserve
                        / "um_runs"
                        / "wasp96b"
                        / "equilibrium"
                        / "u-cp158_tK6"
                    ),
                },
            },
            "mdh_1": {
                "mdh": "1",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium mdh=1 dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp96b"
                    / "initial_profile"
                    / "WASP-96b_PT_EQ_MdH1.ncdf"
                ),
                "star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp96b"
                    / "spectral_files"
                    / "spec_file_wasp96b_mdh1_sw_500"  # spec_file_wasp96b_mdh1_sw_500, spec_file_wasp96b_mdh1_sw_500_2micron
                ),
                "tK_1": {  # retrograde + wrong alkalies
                    "diff_timescale_wind": "1",
                    "rose_suite": "u-cp770_tK1",
                    "dir_for_data": Path(
                        path_to_data_umserve
                        / "um_runs"
                        / "wasp96b"
                        / "equilibrium"
                        / "u-cp770_tK1"
                    ),
                },
                "tK_6": {
                    "diff_timescale_wind": "6",
                    "rose_suite": "u-cp770_tK6",
                    "dir_for_data": Path(
                        path_to_data_umserve
                        / "um_runs"
                        / "wasp96b"
                        / "equilibrium"
                        / "u-cp770_tK6" # _wrong_alkalies
                    ),
                },
            },
        },
        "kinetics": {
            "chemical_scheme": "kinetics",
            "chemical_network": "Venot2019 reduced",
            "mdh_0": {
                "mdh": "0",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium mdh=0 dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp96b"
                    / "initial_profile"
                    / "WASP-96b_PT_EQ.ncdf"
                ),
                "star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp96b"
                    / "spectral_files"
                    / "spec_file_wasp96b_mdh0_sw_500"  # spec_file_wasp96b_mdh0_sw_500 spec_file_wasp96b_mdh0_sw_500_2micron
                ),
                "tK_1": {
                    "diff_timescale_wind": "1",
                    "rose_suite": "u-cp238_tK1",
                    "dir_for_data": Path(
                        path_to_data_umserve
                        / "um_runs"
                        / "wasp96b"
                        / "kinetics"
                        / "u-cp238_tK1"
                    ),
                },
                "tK_6": {
                    "diff_timescale_wind": "6",
                    "rose_suite": "u-cp238_tK6",
                    "dir_for_data": Path(
                        path_to_data_umserve
                        / "um_runs"
                        / "wasp96b"
                        / "kinetics"
                        / "u-cp238_tK6"
                    ),
                },
            },
            "mdh_1": {
                "mdh": "1",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium mdh=1 dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp96b"
                    / "initial_profile"
                    / "WASP-96b_PT_EQ_MdH1.ncdf"
                ),
                "star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp96b"
                    / "spectral_files"
                    / "spec_file_wasp96b_mdh1_sw_500"  # spec_file_wasp96b_mdh1_sw_500, spec_file_wasp96b_mdh1_sw_500_2micron
                ),
                "tK_1": {  # retrograde + wrong alkalies
                    "diff_timescale_wind": "1",
                    "rose_suite": "u-cp805_tK1",
                    "dir_for_data": Path(
                        path_to_data_umserve
                        / "um_runs"
                        / "wasp96b"
                        / "kinetics"
                        / "u-cp805_tK1"
                    ),
                },
                "tK_6": {
                    "diff_timescale_wind": "6",
                    "rose_suite": "u-cp805_tK6",
                    "dir_for_data": Path(
                        path_to_data_umserve
                        / "um_runs"
                        / "wasp96b"
                        / "kinetics"
                        / "u-cp805_tK6" # _wrong_alkalies
                    ),
                },
            },
        },
    },
}

GASES = {
    "He": {"tex": "$He$", "color": "C4"},  # needs changing (C4 as HCN)
    "CH3": {"tex": "$CH_3$"},
    "H": {"tex": "$H$", "color": "C9"},
    "1CH2": {"tex": "$^{1}CH_2$"},
    "H2": {"tex": "$H_2$", "color": "C0"},  # needs chaning (C0 as H2O)
    "CH4": {
        "molar_mass": iris.cube.Cube(
            16.043, units="g mol-1", long_name="CH4 molar mass"
        ),
        "tex": "$CH_4$",
        "color": "C3",
    },
    "O-3P": {"tex": "$O(^{3}P)$"},
    "OH": {"tex": "$OH$"},
    "CO": {
        "molar_mass": iris.cube.Cube(
            28.010, units="g mol-1", long_name="CO molar mass"
        ),
        "tex": "$CO$",
        "color": "C1",
    },
    "3CH2": {"tex": "$^{3}CH_2$"},
    "H2CO": {"tex": "$H_2CO$"},
    "CH3O": {"tex": "$CH_3O$"},
    "H2O": {
        "molar_mass": iris.cube.Cube(
            18.015, units="g mol-1", long_name="H2O molar mass"
        ),
        "tex": "$H_2O$",
        "color": "C0",
    },
    "CH3OH": {"tex": "$CH_3OH$"},
    "CO2": {
        "molar_mass": iris.cube.Cube(
            44.009, units="g mol-1", long_name="CO2 molar mass"
        ),
        "tex": "$CO_2$",
        "color": "C2",
    },
    "HCO": {"tex": "$HCO$"},
    "CH2OH": {"tex": "$CH_2OH$"},
    "NH": {"tex": "$NH$"},
    "NNH": {"tex": "$NNH$"},
    "N2": {"tex": "$N_2$", "color": "C7"},
    "NH2": {"tex": "$NH_2$"},
    "N2H2": {"tex": "$N_2H_2$"},
    "NH3": {
        "molar_mass": iris.cube.Cube(
            17.031, units="g mol-1", long_name="NH3 molar mass"
        ),
        "tex": "$NH_3$",
        "color": "C5",
    },
    "N2H3": {"tex": "$N_2H_3$"},
    "HOCN": {"tex": "$HOCN$"},
    "NCO": {"tex": "$NCO$"},
    "CN": {"tex": "$CN$"},
    "HCN": {
        "molar_mass": iris.cube.Cube(
            27.025, units="g mol-1", long_name="HCN molar mass"
        ),
        "tex": "$HCN$",
        "color": "C4",
    },
    "HNCO": {"tex": "$HNCO$"},
    "H2CN": {"tex": "$H_2CN$"},
}


ABSORBERS = {
    "all": {
        "tex": "All",
        "color": "k",
    },
    "h2_h2_cia": {
        "molar_mass": iris.cube.Cube(2.0158 * 2, units="g mol-1", long_name="H2-H2 molar mass"),
        "tex": "$H_2$-$H_2$ CIA",
        "color": "grey",
    },
    "h2_he_cia": {
        "molar_mass": iris.cube.Cube(
            2.0158 + 4.0026, units="g mol-1", long_name="H2-He molar mass"
        ),
        "tex": "$H_2$-$He$ CIA",
        "color": "lightgrey",
    },
    "li": {
        "molar_mass": iris.cube.Cube(6.941, units="g mol-1", long_name="Li molar mass"),
        "tex": "$Li$",
        "color": "darkred",
    },
    "na": {
        "molar_mass": iris.cube.Cube(22.99, units="g mol-1", long_name="Na molar mass"),
        "tex": "$Na$",
        "color": "gold",
    },
    "k": {
        "molar_mass": iris.cube.Cube(39.098, units="g mol-1", long_name="K molar mass"),
        "tex": "$K$",
        "color": "#C8A2C8",
    },
    "rb": {
        "molar_mass": iris.cube.Cube(85.4678, units="g mol-1", long_name="Rb molar mass"),
        "tex": "$Rb$",
        "color": "violet",
    },
    "cs": {
        "molar_mass": iris.cube.Cube(132.905, units="g mol-1", long_name="Cs molar mass"),
        "tex": "$Cs$",
        "color": "darkslateblue",
    },
    "ch4": {
        "molar_mass": iris.cube.Cube(16.04, units="g mol-1", long_name="CH4 molar mass"),
        "tex": "$CH_4$",
        "color": "C3",
    },
    "co": {
        "molar_mass": iris.cube.Cube(28.01, units="g mol-1", long_name="CO molar mass"),
        "tex": "$CO$",
        "color": "C1",
    },
    "co2": {
        "molar_mass": iris.cube.Cube(44.01, units="g mol-1", long_name="CO2 molar mass"),
        "tex": "$CO_2$",
        "color": "C2",
    },
    "h2o": {
        "molar_mass": iris.cube.Cube(18.015, units="g mol-1", long_name="H2O molar mass"),
        "tex": "$H_2O$",
        "color": "C0",
    },
    "hcn": {
        "molar_mass": iris.cube.Cube(27.025, units="g mol-1", long_name="HCN molar mass"),
        "tex": "$HCN$",
        "color": "C4",
    },
    "nh3": {
        "molar_mass": iris.cube.Cube(17.031, units="g mol-1", long_name="NH3 molar mass"),
        "tex": "$NH_3$",
        "color": "C5",
    },
}