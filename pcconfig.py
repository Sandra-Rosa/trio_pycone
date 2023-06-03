import pynecone as pc

class TriopyconeConfig(pc.Config):
    pass

config = TriopyconeConfig(
    app_name="trio_pycone",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)