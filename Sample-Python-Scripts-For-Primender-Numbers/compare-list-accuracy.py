from collections import Counter

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]
    
def read_comma_separated_numbers(filename):
    with open(filename, 'r') as file:
        return [int(num.strip()) for line in file for num in line.split(',') if num.strip().isdigit()]

def compare_unordered_lists(correct_file, test_file):
    correct_seq = read_numbers_from_file(correct_file)
    test_seq = read_numbers_from_file(test_file)

    counter_correct = Counter(correct_seq)
    counter_test = Counter(test_seq)

    # Get all unique numbers from both
    all_keys = set(counter_correct.keys()).union(set(counter_test.keys()))

    matched = 0
    unmatched = 0

    for key in all_keys:
        correct_count = counter_correct.get(key, 0)
        test_count = counter_test.get(key, 0)
        matched += min(correct_count, test_count)
        unmatched += abs(correct_count - test_count)

    total_expected = sum(counter_correct.values())
    total_tested = sum(counter_test.values())

    error_percent = ((total_expected - matched) / total_expected) * 100 if total_expected else 0

    print("====== Unordered List Comparison ======")
    print("✔ Total Numbers in Correct File: ", total_expected)
    print("✔ Total Numbers in Test File   : ", total_tested)
    print("✅ Matched Elements             : ", matched)
    print("❌ Unmatched Elements           : ", total_expected - matched)
    print("⚠ Error Percentage             : {:.2f}%".format(error_percent))

    # Optional: breakdown of extra/missing items
    missing = counter_correct - counter_test
    extra = counter_test - counter_correct

    if missing:
        print("\n🔻 Missing or less frequent in test file:")
        for num, count in missing.items():
            print(f"  • {num} → Missing {count} time(s)")

    if extra:
        print("\n🔺 Extra or more frequent in test file:")
        for num, count in extra.items():
            print(f"  • {num} → Extra {count} time(s)")

    # Final Summary
    print("\n======= Summary =======")
    print("🔍 Method Used     : Ignore Order – Compare Content")
    print("🧠 Strategy        : Matches frequencies, computes true error")
    print("📊 Metrics         :")
    print(f"   • Total Expected    = {total_expected}")
    print(f"   • Total Tested      = {total_tested}")
    print(f"   • Correct Matches   = {matched}")
    print(f"   • Total Errors      = {total_expected - matched}")
    print(f"   • Error Percentage  = {error_percent:.2f}%")
    print("✅ Suitable for unordered validation with correct proportions.")

compare_unordered_lists('Output/Full-List-primender_sequence_100000.txt', 'Output/deepseek-R1/primender_sequence_terms_to_100001.txt')

