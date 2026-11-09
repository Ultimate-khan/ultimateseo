"""UltimateSEO — evidence-led website crawling, analysis and SEO reporting."""

__version__ = "3.0.0"
__all__ = ["Config", "Crawler", "__version__"]


def __getattr__(name):
    if name == "Config":
        from .network import Config

        return Config
    if name == "Crawler":
        from .engine import Crawler

        return Crawler
    raise AttributeError(name)
