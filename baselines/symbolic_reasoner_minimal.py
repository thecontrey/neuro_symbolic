def reason(facts):
    """Minimal schematic reasoner for the anonymized examples."""
    valid = facts.get("ValidContract(case)", False)
    delay = facts.get("Delay(case)", False)
    fm = facts.get("ForceMajeure(case)", False)
    gross = facts.get("GrossNegligence(case)", False)
    notice_missing = facts.get("NoticeMissing(case)", False)
    notice_waived = facts.get("NoticeWaived(case)", False)
    if not (valid and delay):
        return "Negative"
    if (fm and not gross) or (notice_missing and not notice_waived):
        return "Negative"
    return "Positive"

if __name__ == "__main__":
    print(reason({"ValidContract(case)": True, "Delay(case)": True}))
