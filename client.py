class MultiItemGoalBasketPlannerClient:
    def plan_goal_driven_basket(self, goal_description='Weekend camping trip for two in rainy weather', budget_ceiling_usd=350.00):
        return {
            'basket_plan_id': 'bsk_pln_8812',
            'goal_theme': goal_description,
            'planned_bundle_items': [
                {'category': 'Shelter', 'title': '2-Person 3000mm Waterproof Tent', 'price_usd': 149.00, 'priority': 'MANDATORY'},
                {'category': 'Sleep System', 'title': 'Thermal Insulated Sleeping Pad x2', 'price_usd': 98.00, 'priority': 'MANDATORY'},
                {'category': 'Cookware', 'title': 'Windproof Compact Camp Stove', 'price_usd': 45.00, 'priority': 'RECOMMENDED'}
            ],
            'total_basket_cost_usd': 292.00,
            'budget_variance_remaining_usd': 58.00,
            'bundle_manifest_url': 'https://basket.planner.genpark.ai/bundles/8812.json'
        }
