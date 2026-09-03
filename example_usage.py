from client import MultiItemGoalBasketPlannerClient

def main():
    client = MultiItemGoalBasketPlannerClient()
    res = client.plan_goal_driven_basket('Sourdough bread baking home setup', 200.00)
    print('Goal Basket Planner: ' + res['basket_plan_id'] + ' (' + res['goal_theme'] + ')')
    print('Total Cost: $' + str(res['total_basket_cost_usd']) + ' (Remaining: $' + str(res['budget_variance_remaining_usd']) + ')')
    print('Items: ' + str(len(res['planned_bundle_items'])) + ' items | Manifest URL: ' + res['bundle_manifest_url'])

if __name__ == '__main__':
    main()
