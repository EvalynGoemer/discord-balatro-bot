from modules.utils import build_reply_with_items, parse_items_from_comment
import os

def test_parse_items_from_comment():
    assert ["baron"] == parse_items_from_comment("Use [[baron]]")
    assert ["baron", "mime"] == parse_items_from_comment("Use [[baron]] and [[mime]]")
    assert ["baron", "mime"] == parse_items_from_comment("Use [[baron]] and [[mime]]")
    assert ["baron", "mime"] == parse_items_from_comment("Use \\[\\[baron\\]\\] and \\[\\[mime\\]\\]")
    assert ["baron", "mime"] == parse_items_from_comment("Use \\[[baron]] and \\[[mime]]")
    assert ["mime"] == parse_items_from_comment("Use [[baron] and [[mime]]")
    assert ["baron", "mime"] == parse_items_from_comment("Use [[baron]][[mime]]")
    assert ["baron", "mime"] == parse_items_from_comment("Use [[[baron]]][[[mime]]]")
    assert ["baron", "mime"] == parse_items_from_comment("Use [[baron]], [[]], and [[mime]]")
    assert [] == parse_items_from_comment("[[]], [[]]")

def test_build_reply_with_items():
    os.environ["FANDOM_LINK"] = "http://localhost:8080/"
    os.environ["MAX_DISTANCE"] = "3"
    assert ("[Showman](http://localhost:8080/Showman) (Uncommon Joker)" in build_reply_with_items(["showman"])) is True
    assert ("[Showman](http://localhost:8080/Showman) (Uncommon Joker)" in build_reply_with_items(["showman", "perkeo"])
            and "[Perkeo](http://localhost:8080/Perkeo) (Legendary Joker)" in build_reply_with_items(["showman", "perkeo"])) is True
    assert ("[Cavendish](http://localhost:8080/Cavendish) (Common Joker)" in build_reply_with_items(["cavedise"])) is True
    assert ("" == build_reply_with_items([]))
    assert ("[Overstock](http://localhost:8080/Vouchers) (Voucher)" in build_reply_with_items(["overstock"])) is True
    assert ("[The Magician](http://localhost:8080/Tarot_Cards) (Tarot Card)" in build_reply_with_items(["magician"])) is True
    assert ("[Ankh](http://localhost:8080/Spectral_Cards) (Spectral Card)" in build_reply_with_items(["ankh"])) is True
    assert ("[The Arm](http://localhost:8080/Blinds_and_Antes) (Blind)" in build_reply_with_items(["arm"])) is True
