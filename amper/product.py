from decimal import Decimal
from typing import List


class ProductCategory:
    def __init__(self):
        self.external_id: str = None
        self.parent_external_id: str = None
        self.name: str = None
        self.description: str = ''
        self.seo_tags: str = None
        self.order: int = 1
        self.updatable_fields: str = None


class ProductCategoryRelation:
    def __init__(self):
        self.external_id: str = None
        self.category_external_id: str = None
        self.product_external_id: str = None


class ProductAttributes:
    def __init__(self, key, atr_name, atr_val, enabled_for_filtering=True, show_on_tile=False):
        self.key: str = key
        self.atr_name: str = atr_name
        self.atr_val: str = atr_val
        self.is_b2b: bool = True
        self.is_msf: bool = True
        self.is_b2c: bool = True
        self.enabled_for_filtering: bool = enabled_for_filtering
        self.show_on_tile: bool = show_on_tile


class Product:
    def __init__(self):
        self.attributes: List[ProductAttributes] = []
        self.name: str = None
        self.friendly_name: str = None
        self.short_description: str = None
        self.description: str = None
        self.short_code: str = None
        self.sku: str = None
        self.ean: str = None
        self.brand_short_code: str = None
        self.vat: int = 0
        self.available_on: str = '2020-01-01'
        self.is_published: bool = False
        self.is_featured: bool = False
        self.weight: Decimal = 0.0
        self.default_unit_of_measure: str = None
        self.external_id: str = None
        self.updatable_fields: str = None
        self.cumulative_unit_of_measure: str = None
        self.cumulative_converter: Decimal = 0.0
        self.can_be_split: bool = False
        self.cumulative_unit_ratio_splitter: Decimal = 0.0
        self.unit_roundup: bool = False
        self.default_price: Decimal = 0.0
        self.is_b2b_product: bool = False
        self.is_b2c_product: bool = False
        self.is_msf_product: bool = False
        self.is_b2m_product: bool = False
        self.is_msk_product: bool = False
        self.dimension_unit_of_measure: str = None
        self.dimension_width: Decimal = 0.0
        self.dimension_height: Decimal = 0.0
        self.dimension_depth: Decimal = 0.0
        self.is_product_saleable: bool = False
        self.piggy_bank_budget: Decimal = 0.0
        self.concession_a: Decimal = 0
        self.concession_b: Decimal = 0
        self.concession_c: Decimal = 0
        self.capacity: Decimal = 0.0
        self.sorting_column: str = None
        self.is_bestseller: bool = False
        self.is_for_sale: bool = False
        self.status_description: str = None
        self.minimal_price: Decimal = 0.0
        self.product_subtype: int = 0
        self.sanitized_description: str = None
        self.cn_code: str = None
        self.order: int = 0
