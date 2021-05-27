"""
Cette partie vérifie les paquets externes et les installe s'ils n'existent pas.
"""

requirements = ['pygame']
import sys

# trouver et installer tout paquet externe manquant
def check():
    # trouver les paquets manquants
    from importlib.util import find_spec
    missing = [requirement for requirement in requirements if not(find_spec(requirement))]
    if not missing:
        return
    # installer les paquets manquants
    sys.stdout.write("Installing" + ','.join(missing) + ".\n")
    # redirige vers rien, de sorte qu'aucun message d'installation ne sera vu.
    sys_stdout = sys.stdout
    sys_stderr = sys.stderr
    sys.stdout = None
    sys.stderr = None
    from pip.commands.install import InstallCommand
    from pip.status_codes import SUCCESS
    cmd = InstallCommand()
    for requirement in requirements:
        try:
            if cmd.main([requirement]) is not SUCCESS:
                sys_stderr.write("Can not install " + requirement + ", program aborts.\n")
                sys.exit()
        # cela peut se produire à cause de la redirection de stdout et stderr.
        except AttributeError:
            pass
    # sortie directe retour à la normale
    sys.stdout = sys_stdout
    sys.stderr = sys_stderr
    sys.stdout.write("All packages are installed, starting game...")
    sys.stdout.flush()