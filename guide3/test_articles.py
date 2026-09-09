# Copyright (c) 2026, Guruprasad and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase


class IntegrationTestarticles(IntegrationTestCase):
    """
    Integration tests for articles.
    """

    def test_article_creation(self):
        article = frappe.get_doc({
            "doctype": "articles",
            "title": "My First Test",
            "published": 1
        })

        article.insert()

        self.assertEqual(article.title, "My First Test")
        self.assertTrue(frappe.db.exists("articles", article.name))