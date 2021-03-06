import logging

from . import constants


log = logging.getLogger(__name__)


# Party labels mapped to enum.
# Only use lowercase values as keys, since will normalize values.
PARTY_MAPPING = {
    'democratic': constants.Party.DEMOCRATIC,
    'democrat': constants.Party.DEMOCRATIC,
    'd': constants.Party.DEMOCRATIC,
    'independent': constants.Party.INDEPENDENT,
    'i': constants.Party.INDEPENDENT,
    'republican': constants.Party.REPUBLICAN,
    'r': constants.Party.REPUBLICAN,
}


CHAMBER_MAPPING = {
    'lower': constants.Chamber.LOWER,
    'upper': constants.Chamber.UPPER,
}


def chamber_enum(string):
    """Return `Party` enum for a valid chamber-identifier string."""
    if string is None:
        raise ValueError("Input required for `chamber_enum`")
    chamber = CHAMBER_MAPPING.get(string.lower())
    if chamber is None:
        log.warn(f"Could not determine chamber from {string!r}")
    return chamber


def chamber_label(string):
    """Return user-friendly label for a valid chamber-identifier string."""
    chamber = chamber_enum(string)
    return constants.CHAMBER_LABELS[chamber]


def party_enum(string):
    """Return `Party` enum for a valid party-identifier string."""
    if string is None:
        return constants.Party.UNKNOWN
    party = PARTY_MAPPING.get(string.lower())
    if party is None:
        log.warn(f"Could not determine party from {string!r}")
    return party


def party_label(string):
    """Return user-friendly label for a valid party-identifier string."""
    party = party_enum(string)
    return constants.PARTY_LABELS[party]
