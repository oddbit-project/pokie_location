#
# Script to convert iso3166.tab to sql
#


def escape(src: str) -> str:
    result = src.replace("'", "''")
    return result.replace("\n", "")


def process_iso3166(src_file, dest_file):
    tpl_line = "INSERT INTO country(id_country, name) VALUES('{country}', '{name}');\n"
    contents = []
    with open(src_file, "r") as src:
        for l in src:
            if not l.startswith("#"):
                row = l.split("\t")
                contents.append(
                    tpl_line.format(country=escape(row[0]), name=escape(row[1]))
                )

    with open(dest_file, "w") as dest:
        dest.writelines(contents)


def process_zone(src_file, dest_file):
    tpl_line = "INSERT INTO timezone(id_timezone, fk_country) VALUES('{timezone}', '{country}');\n"
    contents = []
    with open(src_file, "r") as src:
        for l in src:
            if not l.startswith("#"):
                row = l.split("\t")
                contents.append(
                    tpl_line.format(timezone=escape(row[2]), country=escape(row[0]))
                )

    with open(dest_file, "w") as dest:
        dest.writelines(contents)


if __name__ == "__main__":
    print("Generating country.sql...")
    process_iso3166("iso3166.tab", "country.sql")
    print("Generating timezone.sql...")
    process_zone("zone.tab", "timezone.sql")
