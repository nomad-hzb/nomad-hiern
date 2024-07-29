from nomad.config.models.plugins import SchemaPackageEntryPoint


class HIERNPackageEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from nomad_hiern.schema_packages.hiern_package import m_package
        return m_package


hiern_package = HIERNPackageEntryPoint(
    name='HIERN',
    description='Package for HIERN Lab',
)
