# SKPMTF*RNLYOEAUIln$DC

KEYS = (
    'S-', 'K-', 'P-', 'M-', 'T-', 'F-', '*', 'R-', 'N-', 'L-',
    'Y-',
	'-O', '-E', '-A', '-U', '-I', '-l', '-n', '-$', '-D', '-C',
)
IMPLICIT_HYPHEN_KEYS = KEYS

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = 'Ul$C'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        'S-'        : 'q',
        'K-'        : 'a',
        'P-'        : 'w',
        'M-'        : 's',
        'T-'        : 'e',
        'F-'        : 'd',
        '*'        : 'r',
        'R-'        : 'f',
        'N-'        : 't',
        'L-'        : ('g', 'v'),
        'Y-'        : ('h','b','n'),
        '-O'        : 'u',
        '-E'        : ('j', 'm'),
        '-A'        : 'i',
        '-U'        : 'k',
        '-I'        : 'o',
        '-l'        : 'l',
        '-n'        : 'p',
        '-$'        : ';',
        '-D'        : '[',
        '-C'        : "'",
        'arpeggiate': 'space'
    },
	'Stentura': {
        'S-'   : 'S-',
        'K-'   : 'T-',
        'P-'   : 'K-',
        'M-'   : 'P-',
        'T-'   : 'W-',
        'F-'   : 'H-',
        '*'   : 'R-',
        'R-'   : 'A-',
        'N-'   : 'O-',
        'L-'    : '*',
        'Y-'   : '-E',
        '-O'   : '-U',
        '-E'   : '-F',
        '-A'   : '-R',
        '-U'   : '-P',
        '-I'   : '-B',
        '-l'   : '-L',
        '-n'   : '-G',
        '-$'   : '-T',
        '-D'   : '-S',
        '-C'   : '-D',
    },
}

DICTIONARIES_ROOT = 'asset:portuguese_grandjean:portuguese_grandjean:dictionaries'
DEFAULT_DICTIONARIES = (
	'user.json',
)