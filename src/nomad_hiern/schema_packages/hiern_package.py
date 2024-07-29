#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from nomad.metainfo import (
    Quantity,
    Package,
    Section,
    SubSection,
)


from baseclasses import (
    BaseProcess, BaseMeasurement, LayerDeposition, Batch
)


from baseclasses.material_processes_misc import (
    Cleaning,
    SolutionCleaning,
    PlasmaCleaning,
    UVCleaning)
from baseclasses.solar_energy import (
    Substrate,
    JVMeasurement,
    UVvisMeasurement,
    SolcarCellSample, BasicSampleWithID,
)
from baseclasses.solution import Solution, SolutionPreparationStandard
from baseclasses.vapour_based_deposition import (
    Evaporations
)
from baseclasses.wet_chemical_deposition import (
    SpinCoating,
    BladeCoating,
    WetChemicalDeposition
)
from nomad.datamodel.data import EntryData
from nomad.metainfo import (
    SchemaPackage)


m_package = SchemaPackage()


# %% ####################### Entities


class HIERN_Substrate(Substrate, EntryData):
    m_def = Section(
        a_eln=dict(
            hide=[
                'lab_id',
                'users', 'components', 'elemental_composition'],
            properties=dict(
                order=[
                    "name",
                    "substrate",
                    "conducting_material",
                    "solar_cell_area",
                    "pixel_area",
                    "number_of_pixels"])))


class HIERN_Solution(Solution, EntryData):
    m_def = Section(
        a_eln=dict(
            hide=[
                'users', 'components', 'elemental_composition', "method", "temperature", "time", "speed",
                "solvent_ratio", "washing"],
            properties=dict(
                order=[
                    "name",
                    "datetime",
                    "lab_id",
                    "description", "preparation", "solute", "solvent", "other_solution", "additive", "storage"
                ],
            )),
        a_template=dict(
            temperature=45,
            time=15,
            method='Shaker'))

    preparation = SubSection(section_def=SolutionPreparationStandard)


class HIERN_Sample(SolcarCellSample, EntryData):
    m_def = Section(
        a_eln=dict(hide=['users', 'components', 'elemental_composition'], properties=dict(
            order=["name", "substrate", "architecture"])),
        a_template=dict(institute="HIERN"),
        label_quantity='sample_id'
    )


class HIERN_BasicSample(BasicSampleWithID, EntryData):
    m_def = Section(
        a_eln=dict(hide=['users', 'components', 'elemental_composition']),
        a_template=dict(institute="HIERN"),
        label_quantity='sample_id'
    )


class HIERN_Batch(Batch, EntryData):
    m_def = Section(
        a_eln=dict(
            hide=['users', 'samples'],
            properties=dict(
                order=[
                    "name",
                    "export_batch_ids",
                    "csv_export_file"])))


# %% ####################### Cleaning
class HIERN_Cleaning(Cleaning, EntryData):
    m_def = Section(
        a_eln=dict(
            hide=[
                'lab_id',
                'users',
                'end_time', 'steps', 'instruments', 'results'],
            properties=dict(
                order=[
                    "name", "location",
                    "present",
                    "datetime", "previous_process",
                    "batch",
                    "samples"])))

    cleaning = SubSection(
        section_def=SolutionCleaning, repeats=True)

    cleaning_uv = SubSection(
        section_def=UVCleaning, repeats=True)

    cleaning_plasma = SubSection(
        section_def=PlasmaCleaning, repeats=True)


# %% ### Spin Coating
class HIERN_SpinCoating(SpinCoating, EntryData):
    m_def = Section(
        a_eln=dict(
            hide=[
                'lab_id',
                'users',
                'end_time', 'steps', 'instruments', 'results', 'recipe'],
            properties=dict(
                order=[
                    "name", "location",
                    "present",
                    "recipe"
                    "datetime", "previous_process",
                    "batch",
                    "samples",
                    "solution",
                    "layer",
                    "quenching",
                    "annealing"])),
        a_template=dict(
            layer_type="Absorber Layer",
        ))


# %% ### Dip Coating


class HIERN_BladeCoating(BladeCoating, EntryData):
    m_def = Section(
        a_eln=dict(
            hide=[
                'lab_id',
                'users',
                'end_time', 'steps', 'instruments', 'results'],
            properties=dict(
                order=[
                    "name", "location",
                    "present",
                    "datetime",
                    "batch",
                    "samples",
                    "solution",
                    "layer",
                    "quenching",
                    "annealing"])))


# %% ### Evaporation
class HIERN_Evaporation(
        Evaporations, EntryData):
    m_def = Section(
        a_eln=dict(
            hide=[
                'lab_id',
                'users',
                'end_time', 'steps', 'instruments', 'results'],
            properties=dict(
                order=[
                    "name", "location",
                    "present",
                    "datetime",
                    "batch",
                    "samples", "layer"])))


class HIERN_JVmeasurement(JVMeasurement, EntryData):
    m_def = Section(
        a_eln=dict(
            hide=[
                'lab_id', 'solution',
                'users',
                'author',
                'certified_values',
                'certification_institute',
                'end_time', 'steps', 'instruments', 'results',
            ],
            properties=dict(
                order=[
                    "name",
                    "data_file",
                    "active_area",
                    "intensity",
                    "integration_time",
                    "settling_time",
                    "averaging",
                    "compliance",
                    "samples"])),
        a_plot=[
            {
                'x': 'jv_curve/:/voltage',
                'y': 'jv_curve/:/current_density',
                'layout': {
                    "showlegend": True,
                    'yaxis': {
                        "fixedrange": False},
                    'xaxis': {
                        "fixedrange": False}},
            }])


class HIERN_UVvismeasurement(UVvisMeasurement, EntryData):
    m_def = Section(
        a_eln=dict(
            hide=[
                'lab_id',
                'users',
                'location',
                'end_time', 'steps', 'instruments', 'results'],
            properties=dict(
                order=[
                    "name",
                    "data_file",
                    "samples", "solution"])))


# %%####################################### Generic Entries


class HIERN_Process(BaseProcess, EntryData):
    m_def = Section(
        a_eln=dict(
            hide=[
                'lab_id',
                'users',
                'location',
                'end_time', 'steps', 'instruments', 'results'],
            properties=dict(
                order=[
                    "name",
                    "present",
                    "data_file",
                    "batch",
                    "samples"])))

    data_file = Quantity(
        type=str,
        shape=['*'],
        a_eln=dict(component='FileEditQuantity'),
        a_browser=dict(adaptor='RawFileAdaptor'))


class HIERN_WetChemicalDepoistion(WetChemicalDeposition, EntryData):
    m_def = Section(
        a_eln=dict(
            hide=[
                'lab_id',
                'users',
                'location',
                'end_time', 'steps', 'instruments', 'results'],
            properties=dict(
                order=[
                    "name",
                    "present",
                    "datetime", "previous_process",
                    "batch",
                    "samples",
                    "solution",
                    "layer",
                    "quenching",
                    "annealing"])))

    data_file = Quantity(
        type=str,
        shape=['*'],
        a_eln=dict(component='FileEditQuantity'),
        a_browser=dict(adaptor='RawFileAdaptor'))


class HIERN_Deposition(LayerDeposition, EntryData):
    m_def = Section(
        a_eln=dict(
            hide=[
                'lab_id',
                'users',
                'location',
                'end_time', 'steps', 'instruments', 'results'],
            properties=dict(
                order=[
                    "name",
                    "present",
                    "datetime", "previous_process",
                    "batch",
                    "samples",
                    "layer"
                ])))

    data_file = Quantity(
        type=str,
        shape=['*'],
        a_eln=dict(component='FileEditQuantity'),
        a_browser=dict(adaptor='RawFileAdaptor'))


class HIERN_Measurement(BaseMeasurement, EntryData):
    m_def = Section(
        a_eln=dict(
            hide=[
                'lab_id',
                'users',
                'location',
                'end_time', 'steps', 'instruments', 'results'],
            properties=dict(
                order=[
                    "name",
                    "data_file",
                    "samples", "solution"])))

    data_file = Quantity(
        type=str,
        a_eln=dict(component='FileEditQuantity'),
        a_browser=dict(adaptor='RawFileAdaptor'))


m_package.__init_metainfo__()
