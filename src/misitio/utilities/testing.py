from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class MisitioUtilities(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import misitio.utilities
        xmlconfig.file('configure.zcml',
                       misitio.utilities,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        pass

MISITIO_UTILITIES_FIXTURE = MisitioUtilities()
MISITIO_UTILITIES_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(MISITIO_UTILITIES_FIXTURE, ),
                       name="MisitioUtilities:Integration")