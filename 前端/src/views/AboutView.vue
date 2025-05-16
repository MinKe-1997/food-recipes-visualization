
<template>
    <div class="donation-page">
        <div class="donation-header">
            <h1 class="donation-title">{{ title }}</h1>
            <img :src="logo" alt="" class="donation-logo">
        </div>
        <hr>
        <h2 class="donation-subtitle">{{ subtitle }}</h2>
        <div class="donation-section">
            <div class="donation-left">
                <img :src="heartImage" alt="心形图案" class="donation-heart">
            </div>
            <div class="donation-right">
                <p class="donation-text">我们在此为您提供了一种爱心捐赠的方式，将您的善款用于帮助那些需要帮助的人。您的捐赠将直接到达受助者手中，无需经过任何中间机构。感谢您的支持！</p>
                <h3 class="donation-amount-title">请选择您的捐款金额：</h3>
                <div class="donation-amount-list">
                    <button v-for="amount in amounts" :key="amount" class="donation-amount-btn" @click="setSelectedAmount(amount)" :class="{ 'selected': selectedAmount === amount }">{{ formatCurrency(amount) }}</button>
                </div>
                <form class="donation-form" @submit.prevent="submitDonation">
                    <div class="form-group">
                        <label for="name">姓名：</label>
                        <input type="text" id="name" v-model="name" required>
                    </div>
                    <div class="form-group">
                        <label for="email">邮箱：</label>
                        <input type="email" id="email" v-model="email" required>
                    </div>
                    <div class="form-group">
                        <label for="phone">电话：</label>
                        <input type="tel" id="phone" v-model="phone" pattern="[0-9]{10,12}" required>
                    </div>
                    <div class="form-group">
                        <label for="message">留言（选填）：</label>
                        <textarea id="message" v-model="message" rows="4"></textarea>
                    </div>
                    <button type="submit" class="donation-submit-btn" :disabled="!isValid">立即捐赠</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "DonationPage",
        data() {
            return {
                title: "爱心捐赠",
                subtitle: "帮助那些需要帮助的人",
                logo: "../assets/logo.png",
                heartImage: "../assets/img.png",
                amounts: [10, 20, 50, 100, 200],
                selectedAmount: null,
                name: "",
                email: "",
                phone: "",
                message: ""
            };
        },
        methods: {
            setSelectedAmount(amount) {
                this.selectedAmount = amount;
            },
            formatCurrency(amount) {
                return "$" + amount.toFixed(2);
            },
            submitDonation() {
                // 提交表单的逻辑
                // 发送邮件或短信通知管理员或受助者
            }
        },
        computed: {
            isValid() {
                return (
                    this.selectedAmount !== null &&
                    this.name !== "" &&
                    this.email !== "" &&
                    this.phone !== ""
                );
            }
        }
    };
</script>

<style scoped>
    .donation-page {
        max-width: 800px;
        margin: 0 auto;
        padding: 32px 16px;
        font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    }

    .donation-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .donation-title {
        font-size: 36px;
    }

    .donation-logo {
        height: 64px;
    }

    hr {
        border-top: 1px solid #ccc;
        margin: 16px 0;
    }

    .donation-subtitle {
        font-size: 24px;
        font-weight: normal;
        margin-top: 0;
    }

    .donation-section {
        display: flex;
    }

    .donation-left {
        flex: 1;
        text-align: center;
    }

    .donation-right {
        flex: 2;
    }

    .donation-heart {
        max-width: 100%;
        height: auto;
    }

    .donation-text {
        font-size: 18px;
        line-height: 1.5;
    }

    .donation-amount-title {
        font-size: 20px;
        margin: 16px 0;
    }

    .donation-amount-list {
        display: flex;
        flex-wrap: wrap;
    }

    .donation-amount-btn {
        margin-right: 16px;
        margin-bottom: 16px;
        padding: 8px 16px;
        border: none;
        background-color: #eee;
        color: #333;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s;
    }

    .donation-amount-btn:hover,
    .donation-amount-btn.selected {
        background-color: #333;
        color: #fff;
    }

    .form-group {
        display: flex;
        margin-bottom: 16px;
    }

    .form-group label {
        flex: 1;
        margin-right: 16px;
        text-align: right;
        font-size: 18px;
    }

    .form-group input,
    .form-group textarea {
        flex: 2;
        padding: 8px;
        border: none;
        border-bottom: 1px solid #ccc;
        font-size: 18px;
        transition: all 0.3s;
    }

    .form-group input:focus,
    .form-group textarea:focus {
        outline: none;
        border-bottom: 1px solid #333;
    }

    .donation-submit-btn {
        display: block;
        margin: 32px auto;
        padding: 16px 32px;
        border: none;
        background-color: #333;
        color: #fff;
        font-size: 24px;
        font-weight: bold;
        cursor: pointer;
        outline: none;
        transition: all 0.3s;
    }

    .donation-submit-btn:disabled {
        opacity: 0.5;
        cursor: not-allowed;
    }
</style>
