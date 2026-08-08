from sorter import sort_folder


def test_pdf_is_sorted(tmp_path):
    pdf = tmp_path / "homework.pdf"
    pdf.touch()

    sort_folder(tmp_path, False)

    assert (tmp_path / "Documents" / "homework.pdf").exists()
    assert not pdf.exists()

def test_unknown_file_goes_to_other(tmp_path):
    mystery = tmp_path / "mystery.xyz"
    mystery.touch()

    sort_folder(tmp_path, False)

    assert (tmp_path / "Other" / "mystery.xyz").exists()


def test_collision_creates_unique_name(tmp_path):
    source = tmp_path

    documents = source / "Documents"
    documents.mkdir()

    existing = documents / "homework.pdf"
    existing.touch()

    new_file = source / "homework.pdf"
    new_file.touch()

    sort_folder(source, False)

    assert existing.exists()
    assert (documents / "homework (1).pdf").exists()


def test_dry_run_does_not_move_files(tmp_path):
    pdf = tmp_path / "homework.pdf"
    pdf.touch()

    sort_folder(tmp_path, True)

    assert pdf.exists()
    assert not (tmp_path / "Documents" / "homework.pdf").exists()


def test_recursive_sorting(tmp_path):
    school = tmp_path / "school"
    school.mkdir()

    pdf = school / "homework.pdf"
    pdf.touch()

    sort_folder(tmp_path, False)

    assert (tmp_path / "Documents" / "homework.pdf").exists()
    assert not pdf.exists()

def test_excluded_directory_is_untouched(tmp_path):
    excluded = tmp_path / ".git"
    excluded.mkdir()

    pdf = excluded / "important.pdf"
    pdf.touch()

    sort_folder(tmp_path, False)

    assert pdf.exists()
    assert not (tmp_path / "Documents" / "important.pdf").exists()