"""
mysqladmin command - Command
============================

Parsing and extracting data from output of command ``/bin/mysqladmin variables``.
Parsers contained in this module are:

MysqladminVars - command ``/bin/mysqladmin variables``
------------------------------------------------------

"""

from .. import Parser, parser, LegacyItemAccess
from insights.parsers import ParseException
from insights.specs import Specs


@parser(Specs.mysqladmin_vars)
class MysqladminVars(LegacyItemAccess, Parser):
    """
    The output of command ``/bin/mysqladmin variables`` is in mysql table format,
    contains 'Variable_name' and 'Value' two columns.
    This parser will parse the table and set each variable as an class attribute.

    Sample command output::

        +-------------------------------------------------+------------------+
        | Variable_name                                   | Value            |
        +-------------------------------------------------+------------------+
        | aria_block_size                                 | 8192             |
        | aria_checkpoint_interval                        | 30               |
        | aria_checkpoint_log_activity                    | 1048576          |
        | datadir                                         | /var/lib/mysql/  |
        | version                                         | 5.5.56-MariaDB   |
        +-------------------------------------------------+------------------+


    Example:
        >>> output.version
        '5.5.56-MariaDB'
        >>> 'datadir' in output
        True
        >>> output.get('what', '233')
        '233'
        >>> output.getint('aria_block_size', '4096')
        8192
    """
    def parse_content(self, content):
        """
        Parse output content table of command ``/bin/mysqladmin variables``.
        Set each variable as an class attribute.
        """
        if len(content) < 5:
            raise ParseException("Empty or wrong content in table.")

        data = {}
        for l in content[3:-1]:
            lsp = l.split('|')
            if len(lsp) != 4:
                raise ParseException("Unparseable line in table: %s." % l)
            data[lsp[1].strip().lower()] = lsp[2].strip()
        self.data = data

    def getint(self, keyword, default=None):
        """
        Get value for specified keyword, use default if keyword not found.

        Example:

            >>> output.getint('wait_timeout')
            3000
            >>> output.getint('wait_what')
            None
            >>> output.getint('wait_what', 100)
            100

        Args:

            keyword (str): Key to get from ``self.data``.
            default (int): Default value to return if key is not present.

        Returns:

            value (int): Int value of the stored item, or the default if not found.
        """
        if default and not isinstance(default, int):
            raise TypeError("Default value should be int type.")
        v = self.data.get(keyword)
        return int(v) if v and v.isdigit() else default
