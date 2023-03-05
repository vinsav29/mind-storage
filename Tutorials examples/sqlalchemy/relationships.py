# many-to-one

# parent
class AirflowInstance(Table):
    __tablename__ = "airflow_instances"
    id
    airflow_config_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey("paas_configs.id"))
    postgres_config_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey("paas_configs.id"))
    instance_config_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey("instance_configs.id"))

    airflow_config = relationship("PaasConfig", foreign_keys=[airflow_config_id], lazy="selectin")
    postgres_config = relationship("PaasConfig", foreign_keys=[postgres_config_id], lazy="selectin")
    instance_config = relationship("InstanceConfig", back_populates="airflow_instance", cascade="all, delete", passive_deletes=True, lazy="selectin")

# child
class InstanceConfig(Table):
    __tablename__ = "instance_configs"
    id
    airflow_instance = relationship("AirflowInstance", back_populates="instance_config", lazy="selectin")

class PaasConfig(Table):
    __tablename__ = "paas_configs"
    id

